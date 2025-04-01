"""
URL configuration for pagina_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productos.views import CategoriaViewSet
from productos.views import ProductoViewSet
from compra.views import ClienteViewSet
from compra.views import FacturaViewSet
from compra.views import PaisViewSet
from compra.views import PedidoViewSet
from compra.views import PedidoHasProductosViewSet
from proveedores.views import ProveedorViewSet
from usuario.views import UsuarioViewSet

router = DefaultRouter()
router.register('categorias', CategoriaViewSet, 'view_categoria')
router.register('producto', ProductoViewSet, 'view_producto')
router.register('cliente', ClienteViewSet, 'view_cliente')
router.register('factura', FacturaViewSet, 'view_factura')
router.register('pais', PaisViewSet, 'view_pais')
router.register('pedido', PedidoViewSet, 'view_pedido')
router.register('detalle_pedido', PedidoHasProductosViewSet, 'view_PedidoHasProductos')
router.register('proveedor', ProveedorViewSet, 'view_proveedor')
router.register('usuario', UsuarioViewSet, 'view_usuario')

urlpatterns = [
     path('admin/', admin.site.urls),
     path('api-auth/', include('rest_framework.urls')),
     path('api/', include(router.urls)),
]
