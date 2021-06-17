from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#
# @api_view(['GET'])
# def home(request):
#     students = Student.objects.all()
#     student_serializer = StudentSerializer(students, many=True)
#     return Response({'status': 200, 'message': student_serializer.data})
#
#
# @api_view(['POST'])
# def add_student(request):
#     data = request.data
#     print(data['age'])
#     serializer = StudentSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': status.HTTP_200_OK, 'message': serializer.data})
#     else:
#         return Response({'status': status.HTTP_403_FORBIDDEN, 'message': serializer.errors['error'][0]})
#
#
# @api_view(['PUT'])
# def update_student(request, pk):
#     try:
#         student = Student.objects.get(id=pk)
#         data = request.data
#         if 'age' not in data:
#             data['age'] = student.age
#         serializer = StudentSerializer(student, data=data, partial=True)
#         print(data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': status.HTTP_200_OK, 'message': serializer.data})
#         else:
#             return Response({'status': status.HTTP_403_FORBIDDEN, 'message': serializer.errors['error'][0]})
#         # return Response({'status': status.HTTP_403_FORBIDDEN, 'message': 'done'})
#     except ObjectDoesNotExist:
#         return Response({'status': status.HTTP_403_FORBIDDEN, 'message': 'Invalid_id'})
#
#
# @api_view(['DELETE'])
# def delete_student(request, pk):
#     try:
#         student = Student.objects.get(id=pk)
#         student.delete()
#         return Response({'status': status.HTTP_200_OK, 'message': 'Successfully Deleted'})
#     except Exception as e:
#         return Response({'status': status.HTTP_403_FORBIDDEN, 'message': 'Invalid_id'})


@api_view(['GET'])
def books(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status': status.HTTP_200_OK, 'payload': serializer.data})


class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return Response({'status': 200, 'message': student_serializer.data})

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if 'age' in serializer.initial_data:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': status.HTTP_200_OK, 'message': serializer.data})
            else:
                return Response({'status': status.HTTP_403_FORBIDDEN, 'message': serializer.errors['error'][0]})
        else:
            return Response({'status': status.HTTP_403_FORBIDDEN, 'message': 'Please Enter your age'})

    def put(self, request):
        try:
            id = request.data['id']
            student = Student.objects.get(id=id)
            data = request.data
            if 'age' not in data:
                data['age'] = student.age
            serializer = StudentSerializer(student, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': status.HTTP_200_OK, 'message': serializer.data})
            else:
                return Response({'status': status.HTTP_403_FORBIDDEN, 'message': serializer.errors['error'][0]})
        except ObjectDoesNotExist:
            return Response({'status': status.HTTP_403_FORBIDDEN, 'message': 'Invalid_id'})

    def delete(self, request):
        try:
            pk = request.GET.get('id')
            student = Student.objects.get(id=pk)
            student.delete()
            return Response({'status': status.HTTP_200_OK, 'message': 'Successfully Deleted'})
        except Exception as e:
            print(request.GET.get('id'))
            return Response({'status': status.HTTP_403_FORBIDDEN, 'message': 'Invalid_id'})


class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            token = Token.objects.get_or_create(user=user)
            return Response({'status': status.HTTP_200_OK, 'message': serializer.data})
        else:
            return Response({'status': status.HTTP_403_FORBIDDEN, 'message': serializer.errors['error'][0]})
