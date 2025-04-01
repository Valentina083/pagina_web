from rest_framework import viewsets
# modelo creado
from compra.models import Cliente
# serializer creado
from compra.serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
