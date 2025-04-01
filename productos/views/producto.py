from rest_framework import viewsets
# modelo creado
from productos.models import Producto
# serializer creado
from productos.serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
