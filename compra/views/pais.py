from rest_framework.viewsets import ModelViewSet
# modelo creado
from compra.models import Pais
# serializer creado
from compra.serializers import PaisSerializer


class PaisViewSet(ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
