from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    documento = models.CharField(max_length=45, unique=True)
    contacto = models.CharField(max_length=25)
    correo = models.EmailField(max_length=90, unique=True)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=45)
    usuario = models.OneToOneField('usuario.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
