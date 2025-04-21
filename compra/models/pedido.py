from django.db import models
from django.utils import timezone


class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', related_name="pedidos", on_delete=models.CASCADE)
    productos = models.ManyToManyField('productos.Producto', through='pedidoHasProductos' , related_name='pedidos' )
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=5, editable=False)
    valor_total = models.DecimalField(max_digits=10, decimal_places=5, editable=False)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_envio = models.DateTimeField(null=True, blank=True)
    pais_envio = models.CharField(max_length=45)
    estado_orden = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ])
    numero_pedido = models.IntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.numero_pedido:
            # generar número de pedido único
            max_id = Pedido.objects.aggregate(models.Max('numero_pedido'))['numero_pedido__max']
            self.numero_pedido = (max_id or 0) + 1  # Incrementa el último número de pedido

        # agrega fecha de envio cuando ele stado de orden es enviado
        if self.estado_orden == 'enviado' and not self.fecha_envio:
            self.fecha_envio = timezone.now()

        subtotal = sum(ph.subtotal_producto for ph in self.pedidohasproductos_set.all())
        self.subtotal = subtotal
        self.valor_total = subtotal

        super().save(*args, **kwargs)
