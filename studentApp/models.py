from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):

    type = models.CharField(max_length=100, choices = [('Business', 'Business'),('Computing', 'Computing'), ('Engineering', 'Engineering'), ('Medicine', 'Medicine')])
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default = False)
    details = models.TextField()
    date_subimtted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(User, related_name = 'issues', on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.type} Issue in {self.room}'

        
    