from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

 


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name = 'profile'), 
    path('enroll/', views.enroll_student, name='enroll'),
    path('register/<int:module_id>/', views.register_module, name='register_module'),
    path('unregister/<int:module_id>/', views.unregister_module, name='unregister_module'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)