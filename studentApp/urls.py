from . import views 
from django.urls import path, include
from django.contrib.auth import views as auth_views 


#app_name = 'studentApp' 

urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name = 'about'), 
    path('contact/', views.contact, name = 'contact'), 
    path('modules/', views.modules, name = 'modules'), 
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]