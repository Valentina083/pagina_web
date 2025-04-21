from rest_framework.viewsets import ModelViewSet
# modelo creado
from proveedores.models import Proveedor
# serializer creado
from proveedores.serializers import ProveedorSerializer


class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
