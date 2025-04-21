from rest_framework.viewsets import ModelViewSet
# modelo creado
from compra.models import Factura
# serializer creado
from compra.serializers import FacturaSerializer


class FacturaViewSet(ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
