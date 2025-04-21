from rest_framework import serializers
# modelo creado
from productos.models import Talla


class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talla
        fields = '__all__'
