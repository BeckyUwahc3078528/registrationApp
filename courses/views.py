
from django.shortcuts import render, redirect
from .models import Course, Module
from users.models import Profile
from .forms import EnrollmentForm

# Create your views here.
def register_module(request, module_id):
    module = Module.objects.get(id=module_id)
    student = Profile.objects.get(user=request.user)
    student.register_module(module)
    return redirect('courses/registration.html')

def unregister_module(request, module_id):
    module = Module.objects.get(id=module_id)
    student = Profile.objects.get(user=request.user)
    student.unregister_module(module)
    return redirect('studentApp/home.html')


def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll.html', {'form': form})
