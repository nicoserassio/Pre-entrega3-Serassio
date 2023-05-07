from django.shortcuts import render
from taller.models import Cliente, Auto, Turno
from django.http import HttpResponse
from taller.forms import clienteForm

#vista principal
def inicio(request):
    return render(request, 'taller/inicio.html')

#buscar clientes en base de datos
def buscarCliente(request):
    return render(request, 'taller/buscarClientes.html')
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        nombres = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadoClientes.html", {"nombres":nombres, "nombre": nombre})
    else:
        respuesta = "no se encontraron datos"
    return HttpResponse(respuesta)

#mostrar clientes en base de datos
def leerClientes(request):
    clientes = Cliente.objects.all()
    contexto={'clientes':clientes}
    return render(request, 'taller/leerClientes.html', contexto)

#Registro de datos para solicitar turnos que incluyan todos los campos de los modelos
def clienteFormulario(request):
    if request.method == "POST":
        formulario = clienteForm(request.POST)
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
        formulario = clienteForm()
    return render(request, "taller/clienteFormulario.html", {"formulario":formulario})
