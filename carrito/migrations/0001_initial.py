# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cliente', models.CharField(max_length=200)),
                ('tarjeta_credito', models.CharField(max_length=200)),
                ('direccion_entrega', models.TextField()),
                ('telefonos_cliente', models.CharField(max_length=30)),
                ('fecha_compra', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_compra', models.DecimalField(decimal_places=2, max_digits=9)),
                ('autorizo', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('precio_parcial', models.DecimalField(decimal_places=2, max_digits=9)),
                ('cod_compra', models.ForeignKey(to='carrito.Compra')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='cod_producto',
            field=models.ForeignKey(to='carrito.Producto'),
        ),
    ]
