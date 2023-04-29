from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email=models.EmailField(max_length=30)
    auto=models.CharField(max_length=30)

class Auto(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    
class Turno(models.Model):
    servicio=models.CharField(max_length=30)
    tiempo=models.IntegerField() 
    