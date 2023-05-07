from django import forms
 
class clienteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    email= forms.EmailField()
    marca = forms.CharField()
    modelo = forms.CharField()
    dia = forms.DateField()
    hora = forms.IntegerField()
