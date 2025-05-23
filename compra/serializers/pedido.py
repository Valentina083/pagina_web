from rest_framework import serializers
# modelo creado
from compra.models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    productos_info = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'
