from django.contrib import admin
from .models import Profile 

# Register your models here.

admin.site.register(Profile)


# @admin.site.register(Profile)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('user',)
#     filter_horizontal = ('registered_modules',)
