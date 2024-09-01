from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from courses.models import Course
# , Module


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save, sender=Profile)
# def register_default_module(sender, instance, created, **kwargs):
#     if created:
#         default_module = Module.objects.get(name="Introduction to Programming")
#         instance.enrolled_module.add(default_module)