# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0004_remove_compra_autorizo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='cod_compra',
        ),
        migrations.RemoveField(
            model_name='detallecompra',
            name='cod_producto',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='total_compra',
        ),
        migrations.AddField(
            model_name='compra',
            name='cod_producto',
            field=models.ForeignKey(to='carrito.Producto', default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DetalleCompra',
        ),
    ]
