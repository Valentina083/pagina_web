from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    correo = models.CharField(max_length=90)
    contraseña = models.CharField(max_length=20)
    perfil_usuario = models.CharField(max_length=25)
