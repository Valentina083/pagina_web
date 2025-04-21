from rest_framework.viewsets import ModelViewSet
from productos.models import Caracteristica
from productos.serializers import CaracteristicaSerializer


class CaracteristicaViewSet(ModelViewSet):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer
