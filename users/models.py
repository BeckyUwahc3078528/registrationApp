from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/profile_pics/default.png', upload_to='profile_pics')
    # enrolled_course = models.OneToOneField(Course, related_name='enrolled_student', on_delete=models.CASCADE)
    # enrolled_modules = models.ManyToManyField(Course, related_name='enrolled_mod')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def register_module(self, module):
        self.registered_modules.add(module)

    def unregister_module(self, module):
        self.registered_modules.remove(module)