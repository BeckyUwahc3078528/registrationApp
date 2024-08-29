from django.contrib import admin
from .models import Inquiry

# Register your models here.
# from .models import Message



@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_subimtted')
    search_fields = ('name', 'email')
