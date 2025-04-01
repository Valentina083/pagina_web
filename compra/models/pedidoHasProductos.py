from django.db import models
from django.core.validators import MinValueValidator


class PedidoHasProductos(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.PROTECT)
    producto = models.ForeignKey('productos.Producto', null=True, on_delete=models.SET_NULL)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
