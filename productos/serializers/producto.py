from rest_framework import serializers
from productos.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'categoria', 'nombre', 'descripcion', 'imagen', 'estilo', 'precio_unidad', 'cantidad_inventario',
        'materiales', 'tallas_disponibles']