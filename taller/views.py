from django.shortcuts import render
from taller.models import Cliente, Auto, Turno
from django.http import HttpResponse
from taller.forms import ClienteFormulario

def inicio(request):
    return render(request, 'taller/inicio.html')
def clientes(request):
    return render(request, 'taller/clientes.html')
def autos(request):
    return render(request, 'taller/autos.html')
def turnos(request):
    return render(request, 'taller/turnos.html')

def ClienteFormulario(request):
      if request.method == "POST":
            miFormulario = ClienteFormulario(request.POST) 
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']), str(email=informacion['email']))
                  cliente.save()
                  return render(request, "taller/inicio.html")
      else:
            miFormulario = ClienteFormulario()
 
      return render(request, "taller/ClienteFormulario.html", {"miFormulario": miFormulario})