from rest_framework import serializers
# modelo creado
from productos.models import Estilo


class EstiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estilo
        fields = '__all__'
