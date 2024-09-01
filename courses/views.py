
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
# from .models import ModuleRegistration
from users.models import Profile
from .forms import ModuleRegForm

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# View to show details of a specific course and its modules
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = Profile.objects.get(user=request.user)
    return render(request, 'courses/course_detail.html', {'course': course, 'student': student})

# def register_module(request, module_id):
#     module = Module.objects.get(id=module_id)
#     student = Profile.objects.get(user=request.user)
#     student.register_module(module)
#     return redirect('courses/registration.html')

# def unregister_module(request, module_id):
#     module = Module.objects.get(id=module_id)
#     student = Profile.objects.get(user=request.user)
#     student.unregister_module(module)
#     return redirect('studentApp/home.html')


def registermodule_student(request):
    if request.method == 'POST':
        form = ModuleRegForm(request.POST)
        if form.is_valid():
            course = get_object_or_404(Course, id=request.POST.get('course_id'))

            form.save()
            return redirect('registeModule_success')
        else:
            print(form.errors) 
    else:
        form = ModuleRegForm()
    return render(request, 'courses/registerModule.html', {'form': form})

def registeModule_successs(request):
    return render(request, 'courses/registerModule_success.html')
