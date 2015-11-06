# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_auto_20151030_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
