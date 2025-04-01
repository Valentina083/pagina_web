from rest_framework import serializers
# modelo creado
from compra.models import PedidoHasProductos


class PedidoHasProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoHasProductos
        fields = '__all__'
