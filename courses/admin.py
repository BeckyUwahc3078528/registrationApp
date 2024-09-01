from django.contrib import admin
from .models import Course,Module

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Course)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name','code', 'credit', 'category', 'availability', 'get_courses_allowed')
    list_filter = ('courses_allowed',)

    def get_courses_allowed(self, obj):
        return ", ".join([course.name for course in obj.courses_allowed.all()])
    get_courses_allowed.short_description = 'Courses Allowed'
    
admin.site.register(Module,ModuleAdmin)
