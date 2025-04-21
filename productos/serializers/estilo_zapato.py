from rest_framework import serializers
from productos.models.estilo_zapato import EstiloZapato


class EstiloZapatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstiloZapato
        fields = '__all__'
