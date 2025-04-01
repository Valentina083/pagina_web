from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=25)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=25)
    pais = models.ForeignKey('compra.Pais', on_delete=models.SET_NULL, null=True, related_name='proveedores')
    # productos = models.ManyToManyField('productos.Producto', related_name='proveedores')
