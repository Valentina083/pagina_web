from rest_framework.viewsets import ModelViewSet
from productos.models import Detalle
from productos.serializers import DetalleSerializer


class DetalleViewSet(ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer
