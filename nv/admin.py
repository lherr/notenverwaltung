from django.contrib import admin
from .models import Student
from .models import Course
from .models import TakePart

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(TakePart)
