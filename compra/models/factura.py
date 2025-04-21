from django.db import models
from django.utils import timezone


class Factura(models.Model):
    MEDIOS_PAGO = [
        ('tarjeta_credito', 'Tarjeta de Crédito'),
        ('tarjeta_debito', 'Tarjeta de Débito'),
        ('transferencia', 'Transferencia Bancaria'),
        ('paypal', 'PayPal'),
    ]

    pedido = models.OneToOneField('Pedido', on_delete=models.PROTECT, related_name='factura')
    fecha_factura = models.DateTimeField(default=timezone.now)
    numero_factura = models.CharField(max_length=20, unique=True)
    nombre_cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT, related_name='facturas')
    medio_pago = models.CharField(max_length=25, choices=MEDIOS_PAGO)
    valor_total = models.DecimalField(max_digits=10, decimal_places=5)

    def save(self, *args, **kwargs):
        if not self.numero_factura:
            last = Factura.objects.aggregate(models.Max('id'))['id__max'] or 0
            self.numero_factura = f"FAC-{last + 1:05d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.numero_factura} - Pedido: {self.pedido.numero_pedido} - Cliente: {self.nombre_cliente.nombre}"
