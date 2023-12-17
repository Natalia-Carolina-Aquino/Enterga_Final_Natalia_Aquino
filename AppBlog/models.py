import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Knit(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    tecnica = models.CharField(max_length=30)
    material = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="tejidos", null=True, blank=True)
    instrucciones = models.CharField(max_length=5000)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.nombre} \nTécnica de Tejido: {self.tecnica}\nMaterial Utilizado: {self.material}\n{self.descripcion}\n\n Instrucciones:\n{self.instrucciones}\n {self.autor}, {self.fecha}"


class KnitComment(models.Model):
    tejido = models.ForeignKey(Knit, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models. CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.datetime.now())

class Yarn(models.Model):
    nombre = models.CharField(max_length=50)
    material = models.CharField(max_length= 200)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to="hilados", null=True, blank=True)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.nombre}\nComposición: {self.material}\n{self.descripcion}\n{self.autor}, {self.fecha}"


class YarnComment(models.Model):
    hilado = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.datetime.now())

class Accessories(models.Model):
    nombre = models.CharField(max_length=100)
    tecnica = models.CharField(max_length=30)
    material = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="accesorios", null=True, blank=True)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.nombre}\nTécnica de Tejido: {self.tecnica}\nComposición: {self.material}\n{self.descripcion}\n {self.autor}, {self.fecha}"


class AccessoriesComment(models.Model):
    accesorio = models.ForeignKey(Accessories, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500)
    fecha = models.DateTimeField(default=datetime.datetime.now())