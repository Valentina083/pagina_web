# Generated by Django 5.1.7 on 2025-04-20 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_caracteristica_detalle_tallazapato_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstiloZapato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estilos_zapato', to='productos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen_banner', models.ImageField(blank=True, null=True, upload_to='imagenes_categorias/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.estilozapato')),
            ],
        ),
    ]
