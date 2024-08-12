from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
#from django.contrib.auth.decorators import login_required  
from django.shortcuts import render



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

def profile(request):

    return render(request, 'users/profile.html', {'title': 'Student Profile'})




