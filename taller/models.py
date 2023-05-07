from django.db import models

# Create your models here.
class Auto(models.Model):
        marca = models.CharField(max_length=30)
        modelo = models.CharField(max_length=30)
        def __str__(self):
            return f'Marca: {self.marca} - Modelo: {self.modelo}'
        
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=200)
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} - Email: {self.email}'

class Turno(models.Model):
    dia=models.DateField()
    hora=models.IntegerField()
    def __str__(self):
        return f'Dia: {self.dia} - Hora: {self.hora}'