from django.db import models


class TallaZapato(models.Model):
    talla = models.CharField(max_length=10)

    def __str__(self):
        return self.talla
