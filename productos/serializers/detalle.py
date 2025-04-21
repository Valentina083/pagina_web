from rest_framework import serializers
# modelo creado
from productos.models import Detalle

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'
