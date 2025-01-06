from django.db import models


class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True, editable=False)
    imagen = models.ImageField(upload_to='media/entradas/', default='media/entradas/logo.png')


class Banner(models.Model):
    titulo = models.TextField(max_length=200, default="Título.")
    imagen = models.ImageField(upload_to='media/banner/', default='media/banner/banner.png')
    descripcion = models.TextField(max_length=200, default="Descripción.")