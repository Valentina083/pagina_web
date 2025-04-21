from django.db import models
from django.core.validators import RegexValidator


class Talla(models.Model):
    valor = models.CharField(
        max_length=3,
    )

    def __str__(self):
        return self.valor.upper()  # siempre en mayúsculas


"""
from django.db import models


class Talla(models.Model):
    TALLAS = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]

    valor = models.CharField(max_length=4, choices=TALLAS)

    def __str__(self):
        return self.valor

código bueno, tra predeterminado las tallas
"""
