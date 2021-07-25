from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField( max_length=12)
    last_name=models.CharField( max_length=10)
    age =models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    role_number=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    student_id=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=20)
    national_id=models.CharField(max_length=20)
    medical_report=models.CharField(max_length=12)
    language=models.CharField(max_length=20)
    laptop_seriol_number=models.CharField(max_length=15)
    date_of_enrolmenta=models.DateField()
    profile=models.ImageField()
    phone_number=models.CharField(max_length=10)

