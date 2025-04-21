from django.db import models
from .categoria import Categoria
from .talla import Talla
from .estilo import Estilo
from .material import Material


class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=5)
    cantidad_inventario = models.PositiveIntegerField()
    descripcion = models.TextField()
    estilo = models.ForeignKey(Estilo, on_delete=models.SET_NULL, null=True, blank=True)
    materiales = models.ManyToManyField(Material, blank=True)
    tallas_disponibles = models.ManyToManyField(Talla, blank=True)
    imagen = models.ImageField(upload_to='imagenes_productos/', null=True, blank=True)
    proveedor = models.ForeignKey('proveedores.Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
