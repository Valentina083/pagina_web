from django.db import models


class Factura(models.Model):
    pedido = models.OneToOneField('Pedido', on_delete=models.PROTECT, related_name='factura_relacionada')
    fecha_factura = models.DateTimeField()
    nombre_cliente = models.CharField(max_length=25)
    descripcion_pedido = models.CharField(max_length=45)
    medio_pago = models.CharField(max_length=25)
    valor_total = models.DecimalField(max_digits=10, decimal_places=5)
