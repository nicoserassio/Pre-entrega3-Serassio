from django import forms
 
class ClienteFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email= forms.EmailField()
class AutoFormulario(forms.Form):
    id = forms.IntegerField()
    marca = forms.CharField()
    modelo = forms.CharField()
    cliente = forms.CharField()
class TurnoFormulario(forms.Form):
    id = forms.IntegerField()
    dia = forms.CharField()
    hora = forms.IntegerField()