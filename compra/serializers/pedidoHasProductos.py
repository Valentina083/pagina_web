from rest_framework import serializers
# modelo creado
from compra.models import PedidoHasProductos
from productos.serializers import ProductoSerializer


class PedidoHasProductosSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = PedidoHasProductos
        fields = '__all__'
