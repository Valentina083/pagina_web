from rest_framework.viewsets import ModelViewSet  # modelo creado
from django_filters.rest_framework import DjangoFilterBackend
from productos.models import Producto
from productos.serializers import ProductoSerializer  # serializer creado
from productos.filters import ProductoFilter


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all().prefetch_related('materiales', 'tallas_disponibles').select_related('categoria', 'estilo')
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter

    def perform_create(self, serializer):
        serializer.save(proveedor=self.request.user.proveedor)
