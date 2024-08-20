from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Module, Registration
from .forms import RegistrationForm

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_list.html', {'modules': modules})

def register_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.module = module
            registration.save()
            return redirect('module_list')
    else:
        form = RegistrationForm()
    return render(request, 'register_module.html', {'form': form, 'module': module})
