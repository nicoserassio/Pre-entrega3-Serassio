from django import forms
 
class clienteFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    email= forms.EmailField()
    marca = forms.CharField()
    modelo = forms.CharField()
    dia = forms.DateField()
    hora = forms.IntegerField()
class AutoFormulario(forms.Form):
    id = forms.IntegerField()
    marca = forms.CharField()
    modelo = forms.CharField()
class TurnoFormulario(forms.Form):
    id = forms.IntegerField()
    dia = forms.CharField()
    hora = forms.IntegerField()