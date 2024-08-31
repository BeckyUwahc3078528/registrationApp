from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, EnrollmentForm 
from .models import Profile
from courses.models import Course, Module
from .models import Enrollment
from .forms import ModuleRegistrationForm




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!') 
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Student Registration'})

@login_required 

def profile(request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            return redirect('profile')
        else:
     
            u_form = UserUpdateForm(instance = request.user) 
            p_form = ProfileUpdateForm(instance = request.user.profile) 
            context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'} 
            return render(request, 'users/profile.html', context) 
 
# def enroll_student(request):
#     if request.method == 'POST':
#         form = EnrollmentForm(request.POST)
#         if form.is_valid():
#             course = get_object_or_404(Course, id=request.POST.get('course_id'))

#             form.save()
#             return redirect('enroll_success')
#         else:
#             print(form.errors) 
#     else:
#         form = EnrollmentForm()
#     return render(request, 'courses/enroll.html', {'form': form})

def register_modules(request):
    if request.method == 'POST':
        form = ModuleRegistrationForm(request.POST)
        if form.is_valid():
            modules = form.cleaned_data['modules']
            student = request.user.profile  # Assuming Student is linked to User
            for module in modules:
                Enrollment.objects.get_or_create(student=student, module=module)
            return redirect('enroll_success')  # Redirect to a success page
    else:
        form = ModuleRegistrationForm()
    return render(request, 'courses/enroll.html', {'form': form})


def enroll_success(request):
    return render(request, 'courses/enroll_success.html')

def register_module(request, module_id):
    student = get_object_or_404(Profile, user=request.user)
    module = get_object_or_404(Module, id=module_id)
    student.register_module(module)
    return redirect('courses:module_list')

def unregister_module(request, module_id):
    student = get_object_or_404(Profile, user=request.user)
    module = get_object_or_404(Module, id=module_id)
    student.unregister_module(module)
    return redirect('courses:module_list')

@login_required
def view_enrolled_modules(request):
    student = request.user.profile  # Assuming Student is linked to User
    enrollments = Enrollment.objects.filter(student=student)
    student_name = student.user.get_full_name()
    return render(request, 'users/view_enrolled_modules.html', {'enrollments': enrollments, 'student_name': student_name})




