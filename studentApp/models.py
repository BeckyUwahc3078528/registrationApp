from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.        
# class Message(models.Model):

#     name = models.CharField(max_length=100, choices = [('Business', 'Business'),('Computing', 'Computing'), ('Engineering', 'Engineering'), ('Medicine', 'Medicine')])
#     emailAddress = models.CharField(max_length=100)
#     subject = models.TextField()
#     description = models.TextField()
#     author = models.ForeignKey(User, related_name = 'enquiries', on_delete=models.CASCADE)
#     date_subimtted = models.DateTimeField(default=timezone.now)


#     def __str__(self):

#         return f'{self.subject} Enquiry in {self.name}'
    
#     def get_absolute_url(self):

#         return reverse('messageEnquiry_detail', kwargs = {'pk': self.pk})

class Inquiry(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.TextField()
    description = models.TextField()
    date_subimtted = models.DateTimeField(default=timezone.now)


    def __str__(self):

        return f'{self.subject} from {self.name}'