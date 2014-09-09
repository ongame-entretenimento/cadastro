# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(unique=True, max_length=16)),
                ('senha', models.CharField(max_length=32)),
                ('email', models.EmailField(unique=True, max_length=40)),
                ('data_nascimento', models.DateField(verbose_name=b'Data de Nascimento')),
                ('sexo', models.IntegerField(default=0, choices=[(0, b'Masculino'), (1, b'Feminino')])),
                ('confirmado', models.BooleanField(default=0)),
                ('data_cadastro', models.DateTimeField(verbose_name=b'Data de Cadastro')),
                ('cidade', models.ForeignKey(to='usuario.Cidade')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(to='usuario.Estado'),
            preserve_default=True,
        ),
    ]
