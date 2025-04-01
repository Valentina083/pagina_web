from rest_framework import viewsets
# modelo creado
from compra.models import PedidoHasProductos
# serializer creado
from compra.serializers import PedidoHasProductosSerializer


class PedidoHasProductosViewSet(viewsets.ModelViewSet):
    queryset = PedidoHasProductos.objects.all()
    serializer_class = PedidoHasProductosSerializer
