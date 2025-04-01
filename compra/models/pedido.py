from django.db import models


class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    productos = models.ManyToManyField('productos.Producto', through='pedidoHasProductos' , related_name='pedidos' )
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=5)
    valor_total = models.DecimalField(max_digits=10, decimal_places=5)
    fecha_pedido = models.DateTimeField()
    fecha_envio = models.DateTimeField()
    pais_envio = models.CharField(max_length=45)
    estado_orden = models.CharField(max_length=45)
    factura = models.ForeignKey('Factura', on_delete=models.PROTECT, null=True, blank=True, related_name='pedidos')
