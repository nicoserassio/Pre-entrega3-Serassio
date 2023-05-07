from django.urls import path 
from taller import views 

urlpatterns=[

    path('', views.inicio, name="inicio"),
    path('clienteFormulario', views.clienteFormulario, name = "clienteFormulario"),
    path('leerClientes', views.leerClientes, name = 'leerClientes'),
    path('buscarClientes', views.buscarCliente, name = 'buscarClientes'),
    path('buscar/', views.buscar),
    ]