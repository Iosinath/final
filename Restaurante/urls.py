from django.urls import path,include
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('chefs', views.chefs, name='chefs'),
    path('menus', views.menus, name='menus'),
    path('menus/crear', views.crear, name='crear'),
    path('menus/editar', views.editar, name='editar'),
    path('eliminar/<int:ID>/', views.eliminar, name='eliminar'), 
    path('menus/editar/<int:ID>', views.editar, name='editar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
