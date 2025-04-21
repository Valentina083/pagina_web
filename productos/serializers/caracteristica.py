from rest_framework import serializers
# modelo creado
from productos.models import Caracteristica

class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = '__all__'
