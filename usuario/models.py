# -*- coding: utf-8 -*-

from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return self.nome

class Usuario(models.Model):
    SEXO = (
        (0, 'Masculino'),
        (1, 'Feminino'),
    )

    usuario = models.CharField(max_length=16, unique=True)
    senha = models.CharField(max_length=32)
    email = models.EmailField(max_length=40, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    sexo = models.IntegerField(default=0, choices=SEXO)
    cidade = models.ForeignKey(Cidade)
    confirmado = models.BooleanField(default=0)
    hash = models.CharField(max_length=32)
    data_cadastro = models.DateTimeField('Data de Cadastro')

    def __unicode__(self):
        return self.usuario

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class UsuarioPendente(models.Model):
    SEXO = (
        (0, 'Masculino'),
        (1, 'Feminino'),
    )

    usuario = models.CharField(max_length=16, unique=True)
    senha = models.CharField(max_length=32)
    email = models.EmailField(max_length=40, unique=True)
    data_nascimento = models.DateField('Data de Nascimento')
    sexo = models.IntegerField(default=0, choices=SEXO)
    cidade = models.ForeignKey(Cidade)
    confirmado = models.BooleanField(default=0)
    hash = models.CharField(max_length=32)
    data_cadastro = models.DateTimeField('Data de Cadastro')

    def __unicode__(self):
        return self.usuario

    class Meta:
        verbose_name = 'Usuário Pendente'
        verbose_name_plural = 'Usuários Pendentes'
