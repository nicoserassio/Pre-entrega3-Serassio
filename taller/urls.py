from django.urls import path 
from taller import views 

urlpatterns=[

    path('', views.inicio, name="inicio"),
    path('autos', views.autos, name="autos"),
    path('clientes', views.clientes, name="clientes"),
    path('turnos', views.turnos, name="turnos"),
    path('clienteFormulario', views.clienteFormulario, name = "clienteFormulario"),
    path('leerClientes', views.leerClientes, name = 'leerClientes'),
    ]