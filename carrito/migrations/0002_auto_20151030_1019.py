# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='tarjeta_credito',
            field=models.CharField(max_length=100),
        ),
    ]
