from rest_framework.viewsets import ModelViewSet
# modelo creado
from compra.models import PedidoHasProductos
# serializer creado
from compra.serializers import PedidoHasProductosSerializer


class PedidoHasProductosViewSet(ModelViewSet):
    queryset = PedidoHasProductos.objects.all()
    serializer_class = PedidoHasProductosSerializer
