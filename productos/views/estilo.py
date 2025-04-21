from rest_framework.viewsets import ModelViewSet
from productos.models import Estilo
from productos.serializers import EstiloSerializer


class EstiloViewSet(ModelViewSet):
    queryset = Estilo.objects.all()
    serializer_class = EstiloSerializer
