from rest_framework import viewsets
# modelo creado
from compra.models import Pedido
# serializer creado
from compra.serializers import PedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
