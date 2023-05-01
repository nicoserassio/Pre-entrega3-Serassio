from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader 


def saludo(request):
    return HttpResponse("HOLA")
def inicio(self):
    plantilla=loader.get_template('inicio.html')
    return HttpResponse(plantilla)