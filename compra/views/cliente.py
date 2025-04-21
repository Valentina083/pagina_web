from rest_framework.viewsets import ModelViewSet
# modelo creado
from compra.models import Cliente
# serializer creado
from compra.serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
