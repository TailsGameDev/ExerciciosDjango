from django.shortcuts import render
from .models import Usuario
from django.utils.datastructures import MultiValueDictKeyError
import json
from django.http import JsonResponse

def helloApp(request):
    return render(request,'helloApp.html')

def login(request):
    return render(request,'login.html')

def loginSubmit(request):
    objusuario = getUsuario(request)
    if(objusuario):
        return render(request,'loginDeuBom.html',{ 'usuario': objusuario.usuario, 'txtFile': getTxtFile(objusuario) })
    else:
        return render(request,'loginFalhou.html')

def usarServicos(request):
    objusuario = getUsuario(request)
    vnovasenha = request.POST['novasenha']

    if(objusuario):
        if(vnovasenha != ''):
            objusuario.senha = vnovasenha
        try:
            vfile = request.FILES['file']
            objusuario.file = vfile
        except MultiValueDictKeyError:
            pass
        objusuario.save()
        return render(request, 'loginDeuBom.html', { 'usuario': objusuario.usuario, 'txtFile': getTxtFile(objusuario) })
    else:
        return render(request, 'loginFalhou.html')

def criarUsuario(request):
    vusuario = request.POST['usuario']
    if (Usuario.objects.filter(usuario=vusuario)):
        return(render(request,'erroCriarUsuario.html'))
    else:
        Usuario.objects.create(
            usuario = vusuario,
            senha = request.POST['senha'],
        )
        return render(request,'usuarioCriado.html')

def getUsuario(request):
    vusuario = request.POST['usuario']
    vsenha = request.POST['senha']
    listUsers = Usuario.objects.filter(usuario=vusuario, senha=vsenha)
    usuario = None
    if (len(listUsers) > 0):
        usuario = listUsers[0]
    return usuario

def getTxtFile(usuario):
    txt = ''
    try:
        file = open(usuario.file.name, 'r') 
        txt = file.read()
    except IOError:
        pass
    except UnboundLocalError:
        pass
    
    return txt

def getUsuarios(request):
    return JsonResponse(list(map(Usuario.getDict,Usuario.objects.all())), safe=False)