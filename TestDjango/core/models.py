from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Tema(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)  # El campo autor debe existir
    titulo = models.CharField(max_length=200)
    content = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
    




class Solicitud(models.Model):
    RETIRO_AGUAS = 'retiro_aguas_piscina'
    RETIRO_ARBOLES = 'retiro_arboles'

    TIPO_SOLICITUD_CHOICES = [
        (RETIRO_AGUAS, 'Retiro de aguas de piscinas'),
        (RETIRO_ARBOLES, 'Retiro de árboles'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_solicitud = models.CharField(max_length=50, choices=TIPO_SOLICITUD_CHOICES)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)
    fecha_retiro = models.DateField()
    cantidad_arboles = models.IntegerField(null=True, blank=True)
    cantidad_litros = models.IntegerField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        
        return f'{self.nombre} {self.apellido}'



class Register(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=100)
    confirmar_contrasena = models.CharField(max_length=100)

    def str(self):
        return self.nombre



