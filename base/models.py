from django.db import models
from datetime import date


class Subject(models.Model):
    name = models.CharField(max_length=30)
    subject_code = models.IntegerField(unique=True)


class Teacher(models.Model):
    initials = models.CharField(max_length=10, default="")
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    sir_name = models.CharField(max_length=20)
    tac_number = models.CharField(max_length=20)
    subjects = models.ManyToManyField(Subject)
    age = models.IntegerField()
    employment_date = models.DateField(default=date.today)


class Student(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    subjects = models.ManyToManyField(Subject)
    admission_no = models.IntegerField(null=True)
    admissionDate = models.DateField(auto_now=True)
