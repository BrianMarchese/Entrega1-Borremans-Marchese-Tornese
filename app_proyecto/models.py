from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre= models.CharField(max_length=50)
    tipo_animal= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+str(self.tipo_animal)

class Persona(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.edad)

class Auto(models.Model):
    marca= models.CharField(max_length=50)
    anio_fabricacion= models.DateField()
    modelo= models.CharField(max_length=50)

    def __str__(self):
        return self.marca+" "+str(self.anio_fabricacion) +' '+str(self.modelo)