from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here. 

class Inquiry(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    date_subimtted = models.DateTimeField(default=timezone.now)


    def __str__(self):

        return f'{self.subject} from {self.name}'