from rest_framework.viewsets import ModelViewSet
from productos.models import Talla
from productos.serializers import TallaSerializer


class TallaViewSet(ModelViewSet):
    queryset = Talla.objects.all()
    serializer_class = TallaSerializer
