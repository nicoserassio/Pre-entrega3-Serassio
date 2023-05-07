from django.shortcuts import render
from taller.models import Cliente, Auto, Turno
from django.http import HttpResponse
from taller.forms import clienteFormulario

def inicio(request):
    return render(request, 'taller/inicio.html')
def clientes(request):
    return render(request, 'taller/clientes.html')
def autos(request):
    return render(request, 'taller/autos.html')
def turnos(request):
    return render(request, 'taller/turnos.html')

def leerClientes(request):
    clientes = Cliente.objects.all()
    contexto={'clientes':clientes}
    return render(request, 'taller/leerClientes.html', contexto)

def clienteFormulario(request):
    if request.method == "POST":
        formulario = clienteFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            cliente = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"], telefono=informacion["telefono"],email=informacion["email"])
            auto = Auto(marca=informacion["marca"], modelo=informacion["modelo"])
            turno = Turno(dia=informacion["dia"], hora=informacion["hora"])
            cliente.save()
            auto.save()
            turno.save()
            return render(request, "taller/inicio.html")
    else:
        formulario = clienteFormulario()
    return render(request, "taller/clienteFormulario.html", {"formulario":formulario})
