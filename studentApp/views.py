from django.shortcuts import render
from django.http import HttpResponse 

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