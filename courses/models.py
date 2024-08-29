from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth.models import Group
# from users.models import Profile




class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.course.name})"

# class Module(models.Model):
#     course = models.ForeignKey(Group, related_name='modules', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.name} ({self.course.name})"
    
# class Enrollment(models.Model):
#     student = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     enrollment_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.student.user.username} enrolled in {self.module.name}"
