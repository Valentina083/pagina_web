from rest_framework.viewsets import ModelViewSet
# modelo creado
from compra.models import Pedido
# serializer creado
from compra.serializers import PedidoSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
