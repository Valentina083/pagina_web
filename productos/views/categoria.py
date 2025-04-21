from rest_framework.viewsets import ModelViewSet  # modelo creado
from productos.models import Categoria  # serializer creado
from productos.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
