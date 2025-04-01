from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    documento_id = models.CharField(max_length=45)
    contacto = models.CharField(max_length=25)
    correo = models.CharField(max_length=90)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=45)
    usuario = models.OneToOneField('usuario.Usuario', on_delete=models.CASCADE)
