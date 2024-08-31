from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.urls import path, include
from django.contrib.auth import views as auth_views 
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from courses.views import course_list,course_detail


#app_name = 'studentApp' 

urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name = 'about'), 
    path('courses/', course_list, name = 'courseList'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('contact/', views.submit_inquiry, name = 'submit_inquiry'), 
    path('inquiry/', views.submit_inquiry, name='submit_inquiry'),
    path('inquiry/success/', views.inquiry_success, name='inquiry_success'),

    # path('enquiry/', views.enquiry, name = 'enquiry'), 
    # path('enquiry/', PostListView.as_view(), name = 'enquiry'), 
    # path('messages/<int:pk>', PostDetailView.as_view(), name = 'messageEnquiry_detail'), 
    # path('message/new', PostCreateView.as_view(), name = 'message-create'),
    # path('message/<int:pk>/update/', PostUpdateView.as_view(), name = 'message-update'),

    

  
    
]