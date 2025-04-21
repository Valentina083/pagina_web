from rest_framework import serializers
# modelo creado
from productos.models import TallaZapato


class TallaZapatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TallaZapato
        fields = '__all__'
