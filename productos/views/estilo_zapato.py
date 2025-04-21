from rest_framework.viewsets import ModelViewSet
from productos.models.estilo_zapato import EstiloZapato
from productos.serializers.estilo_zapato import EstiloZapatoSerializer

class EstiloZapatoViewSet(ModelViewSet):
    queryset = EstiloZapato.objects.all()
    serializer_class = EstiloZapatoSerializer
