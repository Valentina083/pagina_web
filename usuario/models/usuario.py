from django.db import models


class Usuario(models.Model):
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
    ]

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    correo = models.CharField(max_length=90, unique=True)
    contraseña = models.CharField(max_length=20)
    perfil_usuario = models.BooleanField(default=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    documento = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
