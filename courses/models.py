from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Module(models.Model):
    CATEGORY_CHOICES = [
        ('CORE', 'Core'),
        ('ELECTIVE', 'Elective'),
        ('OPTIONAL', 'Optional'),
    ]

    AVAILABILITY_CHOICES = [
        ('OPEN', ' open for registration'),
        ('CLOSED', 'Closed'),
    ]

    
    name = models.CharField(max_length=255, default='Enter Module')
    code = models.CharField(max_length=10, default = 0)
    credit = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='CORE')
    description = models.TextField(default=' description')
    availability = models.CharField(max_length=10, choices=AVAILABILITY_CHOICES, default='CLOSED')
    courses_allowed = models.ManyToManyField('Course', related_name='modules', blank=True)
   
    def __str__(self):
        return f"{self.name} ({self.code})"

    
class ModuleRegistration(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.module.name}"