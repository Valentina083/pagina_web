from rest_framework.viewsets import ModelViewSet
# modelo creado
from usuario.models import Usuario
# serializer creado
from usuario.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
