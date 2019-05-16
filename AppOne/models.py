from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=90)

    age=models.IntegerField(default=10,null=False)

    address=models.CharField(max_length=100)

    phone_number=models.CharField(max_length=15)

    height=models.CharField(max_length=5,default='5.9')

class School(models.Model):
    name=models.CharField(max_length=100)

    grade=models.CharField(max_length=20)

    age = models.IntegerField(default=10, null=False)

    address = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)
