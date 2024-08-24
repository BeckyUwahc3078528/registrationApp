from . import views 
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


#app_name = 'studentApp' 

urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name = 'about'), 
    path('contact/', views.contact, name = 'contact'), 
    path('modules/', views.modules, name = 'modules'),
    # path('enquiry/', views.enquiry, name = 'enquiry'), 
    path('enquiry/', PostListView.as_view(), name = 'enquiry'), 
    path('messages/<int:pk>', PostDetailView.as_view(), name = 'messageEnquiry_detail'), 
    path('message/new', PostCreateView.as_view(), name = 'message-create'),
    path('message/<int:pk>/update/', PostUpdateView.as_view(), name = 'message-update'),

  
    
]