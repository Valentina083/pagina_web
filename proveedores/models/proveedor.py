from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30, blank=True)
    correo = models.EmailField(max_length=100, blank=True)
    direccion = models.CharField(max_length=150, blank=True)
    pais = models.ForeignKey('compra.Pais', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
