from django.db import models
from django.contrib.auth.models import User

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    rangoEdad = models.CharField(max_length=30)
    precio = models.FloatField()
    stock = models.FloatField()

def __str__(self):
 return f"{self.nombre} - {self.marca}"   
    
class Servicios(models.Model):
    servicio= models.CharField(max_length=30)
    horarios= models.CharField(max_length=50)
    whatsapp = models.IntegerField()
    
class Contacto(models.Model):
    sucursal = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email= models.EmailField()    
    

   
class Avatar(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 imagen = models.ImageField(upload_to='avatares', null=True, blank = True)


