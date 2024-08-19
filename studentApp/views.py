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



 #def status(request):
    # Get all reported issues
     #Courses = Course.objects.all()

    # Create a context dictionary to pass to the template
     #context = {'course': Course}

    # Render the report.html template with the context
     #return render(request, 'studentApp/status.html', context)
