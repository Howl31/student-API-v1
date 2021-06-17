"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('students/', views.StudentAPI.as_view(), name='students'),
    path('register/', views.Register.as_view(), name='register'),
    # path('add_student', views.add_student, name='add_student'),
    # path('update_student/<int:pk>', views.update_student, name='update_student'),
    # path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
]
