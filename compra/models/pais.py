from django.db import models


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=80)
