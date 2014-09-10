# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import Http404, HttpResponse
from django.core.validators import validate_email
from usuario.models import Usuario, UsuarioPendente, Cidade
import datetime, hashlib

def cadastro(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('base.html', c)

def cadastrar(request):
    #import ipdb; ipdb.set_trace()

    if not request.POST:
        raise Http404

    usuario = request.POST['usuario'].strip()
    senha = request.POST['senha'].strip()
    confirmacao_senha = request.POST['confirmacao_senha'].strip()
    email = request.POST['email'].strip()
    confirmacao_email = request.POST['confirmacao_email'].strip()
    dia = request.POST['dia'].strip()
    mes = request.POST['mes'].strip()
    ano = request.POST['ano'].strip()
    sexo = request.POST['sexo'].strip()
    cidade = request.POST['cidade'].strip()

    if not usuario:
        return HttpResponse("sem_usuario")

    if not senha:
        return HttpResponse("sem_senha")

    if senha != confirmacao_senha:
        return HttpResponse("senhas_diferentes")

    if not email:
        return HttpResponse("sem_email")

    if email != confirmacao_email:
        return HttpResponse("emails_diferentes")

    if not dia:
        return HttpResponse("sem_dia")

    if not mes:
        return HttpResponse("sem_mes")

    if not ano:
        return HttpResponse("sem_ano")

    if not sexo:
        return HttpResponse("sem_sexo")

    if not cidade:
        return HttpResponse("sem_cidade")

    try:
        cidade = Cidade.objects.get(nome=cidade)

    except:
        return HttpResponse('erro_cidade')

    try:
        usuario_existe = Usuario.objects.get(usuario=usuario)
        return HttpResponse('usuario_existe')

    except:
        try: 
            email_existe = Usuario.objects.get(email=email)
            return HttpResponse('email_existe')

        except:
            try:
                usuario_pendente_existe = UsuarioPendente.objects.get(usuario=usuario)
                return HttpResponse('usuario_existe')

            except:
                try: 
                    email_pendente_existe = UsuarioPendente.objects.get(email=email)
                    return HttpResponse('email_existe')

                except:
                    pass

    try:
        usuarioPendente = UsuarioPendente()

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        usuarioPendente.usuario = usuario
        usuarioPendente.senha = hashlib.md5(senha).hexdigest()
        usuarioPendente.email = email
        usuarioPendente.data_nascimento = datetime.datetime(ano, mes, dia)
        usuarioPendente.sexo = sexo
        usuarioPendente.cidade = cidade
        usuarioPendente.data_cadastro = datetime.datetime.now()
        usuarioPendente.hash = hashlib.md5(email).hexdigest()
        usuarioPendente.save()

        return HttpResponse('ok')

    except:
        return HttpResponse('erro_cadastro')

def ativar(request, codigo):
    #import ipdb; ipdb.set_trace()

    try:
        usuarioPendente = UsuarioPendente.objects.get(hash=codigo)

    except:
        raise Http404

    usuario = Usuario()

    usuario.usuario = usuarioPendente.usuario
    usuario.senha = usuarioPendente.senha
    usuario.email = usuarioPendente.email
    usuario.data_nascimento = usuarioPendente.data_nascimento
    usuario.sexo = usuarioPendente.sexo
    usuario.cidade = usuarioPendente.cidade
    usuario.data_cadastro = usuarioPendente.data_cadastro
    usuario.save()

    usuarioPendente.delete()

    return HttpResponse(codigo)

