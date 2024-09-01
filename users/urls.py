from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


 


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name = 'profile'), 
    # path('enroll/', views.register_student, name='enroll'),
    # PUT BACK path('enroll/', views.register_modules, name='register_student'),
    # path('register_success/', TemplateView.as_view(template_name='register_success.html'), name='register_success'),
    # PUT BACKpath('register_success/', views.register_success, name='register_success'),
    # PUT BACKpath('view_enrolled_modules/', views.view_enrolled_modules, name='view_enrolled_modules'),
# put back
    # path('register/<int:module_id>/', views.register_module, name='register_module'),
    # path('unregister/<int:module_id>/', views.unregister_module, name='unregister_module'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)