from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=5)
    cantidad_inventario = models.PositiveIntegerField()
    descripcion = models.TextField()
    # foto_producto = models.CharField(max_length=45)
    proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
