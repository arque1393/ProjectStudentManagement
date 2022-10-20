from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(
        choices=(('CSE', 'CSE'), ('ME', 'ME'), ('ECE', 'ECE'), ('EE', 'EE')),
        null=True, max_length=5)
    roll_no = models.PositiveIntegerField(null=True)
    # contuct_no =


class Faculty (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(
        choices=(('CSE', 'CSE'), ('ME', 'ME'), ('ECE', 'ECE'), ('EE', 'EE')),
        null=True, max_length=5)
    age = models.PositiveIntegerField(null=True)
    salary = models.PositiveIntegerField(null=True)
