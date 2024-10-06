from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name = 'Tienda'),
]

#el name tiene que coincidir con el nombre de url de base.html 
# (la 1ra. en mayus)