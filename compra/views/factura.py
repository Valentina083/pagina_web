from rest_framework import viewsets
# modelo creado
from compra.models import Factura
# serializer creado
from compra.serializers import FacturaSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
