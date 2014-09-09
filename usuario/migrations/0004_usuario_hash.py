# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20140909_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='hash',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
