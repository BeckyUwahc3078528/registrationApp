from django.shortcuts import render
from django.http import HttpResponse 
from .models import Message

# Create your views here.
def home(request): 

  return render(request, 'studentApp/home.html', {'title': 'Welcome'})


def about(request): 

  return render(request, 'studentApp/about.html', {'title': 'About'})


def contact(request): 

  return render(request, 'studentApp/contact.html', {'title': 'Contact'})

def modules(request): 

  return render(request, 'studentApp/modules.html', {'title': 'Modules'})

def register(request): 

  return render(request, 'studentApp/register.html', {'title': 'register'})



def enquiry(request):
   # Get all reported issues
  #Create a context dictionary to pass to the template
  #Render the report.html template with the context
  daily_enquiry = {'messages': Message.objects.all(), 'title': 'Enquiries Reported'}
  return render(request, 'studentApp/enquiry.html', daily_enquiry)
