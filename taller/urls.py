from django.urls import path 
from taller import views 

urlpatterns=[

    path('', views.inicio, name="inicio"),
    path('autos', views.autos, name="autos"),
    path('clientes', views.clientes, name="clientes"),
    path('turnos', views.turnos, name="turnos"),
    path('ClienteFormulario', views.ClienteFormulario, name = "ClienteFormulario")
    ]