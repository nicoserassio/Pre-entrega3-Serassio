from django.db import models

# Create your models here.
class Auto(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    cliente=models.CharField(max_length=50)

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField()

class Turno(models.Model):
    dia=models.CharField
    hora=models.IntegerField