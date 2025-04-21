from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    imagen_banner = models.ImageField(upload_to='imagenes_categorias/', null=True, blank=True)

    def __str__(self):
        return self.nombre
