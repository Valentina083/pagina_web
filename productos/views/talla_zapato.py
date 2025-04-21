from rest_framework.viewsets import ModelViewSet
from productos.models import TallaZapato
from productos.serializers import TallaZapatoSerializer


class TallaZapatoViewSet(ModelViewSet):
    queryset = TallaZapato.objects.all()
    serializer_class = TallaZapatoSerializer
