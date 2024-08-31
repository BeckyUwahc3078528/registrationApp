from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


 


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name = 'profile'), 
    # path('enroll/', views.enroll_student, name='enroll'),
    path('enroll/', views.register_modules, name='enroll_student'),
    # path('enroll_success/', TemplateView.as_view(template_name='enroll_success.html'), name='enroll_success'),
    path('enroll_success/', views.enroll_success, name='enroll_success'),
    path('view_enrolled_modules/', views.view_enrolled_modules, name='view_enrolled_modules'),

    path('register/<int:module_id>/', views.register_module, name='register_module'),
    path('unregister/<int:module_id>/', views.unregister_module, name='unregister_module'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)