from rest_framework import viewsets
# modelo creado
from compra.models import Pais
# serializer creado
from compra.serializers import PaisSerializer


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
