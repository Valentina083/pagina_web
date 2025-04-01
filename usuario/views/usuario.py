from rest_framework import viewsets
# modelo creado
from usuario.models import Usuario
# serializer creado
from usuario.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
