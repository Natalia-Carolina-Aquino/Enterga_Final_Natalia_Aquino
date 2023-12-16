from django.db import models


# Create your models here.
class Knit(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    tecnica = models.CharField(max_length=30)
    material = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField()
    instrucciones = models.CharField(max_length=5000)
    autor = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre} \nTécnica de Tejido: {self.tecnica}\nMaterial Utilizado: {self.material}\n{self.descripcion}\n\n Instrucciones:\n{self.instrucciones}\n {self.autor}, {self.fecha}"


class Yarn(models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length= 200)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField()
    autor = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre}\nComposición: {self.material}\n{self.descripcion}\n{self.autor}, {self.fecha}"


class Accessories(models.Model):
    nombre = models.CharField(max_length=100)
    tecnica = models.CharField(max_length=30)
    material = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField()
    autor = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre}\nTécnica de Tejido: {self.tecnica}\nComposición: {self.material}\n{self.descripcion}\n {self.autor}, {self.fecha}"