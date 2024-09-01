from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


 


urlpatterns = [
    # path('registration/', views.register_module, name='register_module'),
    # path('', views.unregister_module, name = 'unregister_module'),
    # path('registermodule/', views.registermodule_student, name='registermodule'),
    # path('modules/', views.ModuleListView.as_view(), name='module_list'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




