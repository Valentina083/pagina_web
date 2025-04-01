from rest_framework import serializers
# modelo creado
from compra.models import Pais


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'
