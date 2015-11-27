# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_detallecompra_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='autorizo',
        ),
    ]
