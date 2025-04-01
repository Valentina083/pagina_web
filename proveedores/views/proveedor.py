from rest_framework import viewsets
# modelo creado
from proveedores.models import Proveedor
# serializer creado
from proveedores.serializers import ProveedorSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
