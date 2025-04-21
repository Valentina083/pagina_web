from django.db import models


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=80)
    codigo_pais = models.CharField(max_length=3, unique=True)  

    def save(self, *args, **kwargs):
        if not self.codigo_pais:
            self.codigo_pais = self.nombre_pais[:3].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_pais
