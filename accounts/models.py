from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)