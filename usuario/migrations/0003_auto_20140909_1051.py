# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuariopendente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuariopendente',
            options={'verbose_name': 'Usu\xe1rio Pendente', 'verbose_name_plural': 'Usu\xe1rios Pendentes'},
        ),
        migrations.AddField(
            model_name='usuariopendente',
            name='hash',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
