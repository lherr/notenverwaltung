from django.db import models
from django.conf import settings

# Create your models here.

class Student(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_level = models.IntegerField()
    
class Course(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    class_level = models.IntegerField()
    