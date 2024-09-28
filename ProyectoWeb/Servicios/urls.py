from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.servicios, name = 'Servicios'),
]


#esta linea aniade una ruta url adicional que permite a Django servir archivos de medios
#durante el desarrollo 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)