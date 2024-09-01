from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/profile_pics/default.png', upload_to='profile_pics')
    # enrolled_course = models.ForeignKey(Course, default = 1, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default=date(2000, 1, 1))
    address = models.CharField(max_length=255, default="123 Default Street")
    city = models.CharField(max_length=100, default="Default City")
    country = models.CharField(max_length=100, default="Default Country")
    # registered_modules = models.ManyToManyField(Module, related_name='registered_students', blank=True)
    # enrolled_course = models.OneToOneField(Course, related_name='enrolled_student', on_delete=models.CASCADE)
    # enrolled_modules = models.ManyToManyField(Course, related_name='enrolled_mod')
    # put back fom here
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name},{self.date_of_birth} {self.address}, {self.city}, {self.country}'
    
    # def register_module(self, module):
    #     self.registered_modules.add(module)

    # def unregister_module(self, module):
    #     self.registered_modules.remove(module)

    

