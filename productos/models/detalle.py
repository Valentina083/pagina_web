from django.db import models


class Detalle(models.Model):
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion
