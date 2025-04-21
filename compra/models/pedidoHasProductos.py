from django.db import models
from django.core.validators import MinValueValidator


class PedidoHasProductos(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.PROTECT)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE) 
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    subtotal_producto = models.DecimalField(max_digits=10, decimal_places=5, editable=False)  # guarda el subtotal
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=5)

    def save(self, *args, **kwargs):
        # Calcula el subtotal antes de guardar
        self.subtotal_producto = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.pedido.id} - Producto {self.producto.id}"
