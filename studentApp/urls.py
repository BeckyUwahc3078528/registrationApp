from . import views 
from django.urls import path, include
from django.contrib.auth import views as auth_views 


#app_name = 'studentApp' 

urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name = 'about'), 
    path('contact/', views.contact, name = 'contact'), 
    path('modules/', views.modules, name = 'modules'),
     path('status/', views.modules, name = 'status'),  
    
]