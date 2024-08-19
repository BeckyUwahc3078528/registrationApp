from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length= 10)
    credit = models.IntegerField()
    category = models.CharField(max_length= 10)
    description = models.TextField()
    availability = models.BooleanField(default= 'yes')
    allowedCourses = models.BooleanField(default= 'no')

    def __str__(self):
        return self.name

class Registration(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.module.name}"
