import django_filters
from .models import Producto


class ProductoFilter(django_filters.FilterSet):
    categoria = django_filters.CharFilter(field_name='categoria__nombre', lookup_expr='iexact')
    estilo = django_filters.CharFilter(field_name='estilo__nombre', lookup_expr='iexact')
    materiales = django_filters.CharFilter(field_name='materiales__nombre', lookup_expr='iexact')
    tallas_disponibles = django_filters.CharFilter(field_name='tallas_disponibles__nombre', lookup_expr='iexact')

    class Meta:
        model = Producto
        fields = ['categoria', 'estilo', 'materiales', 'tallas_disponibles']


"""
Pendinete de validar esta carpeta
"""
