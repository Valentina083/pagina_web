from rest_framework.viewsets import ModelViewSet
from productos.models import Material
from productos.serializers import MaterialSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


"""
solo estoy colocando el de men, women y beach
queda faltando crear aparte el material de accessories y footwear
"""
