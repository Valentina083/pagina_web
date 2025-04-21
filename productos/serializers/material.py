from rest_framework import serializers
# modelo creado
from productos.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
