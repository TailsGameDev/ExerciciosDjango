from django.shortcuts import render
from .models import Usuario

def helloApp(request):
    return render(request,'helloApp.html')

def login(request):
    return render(request,'login.html')

def loginSubmit(request):
    objusuario = getUsuario(request)
    if(objusuario):
        return render(request,'loginDeuBom.html',{ 'usuario': objusuario.usuario })
    else:
        return render(request,'loginFalhou.html')

def alterarSenha(request):
    objusuario = getUsuario(request)
    vnovasenha = request.POST['novasenha']
    if(objusuario):
        objusuario.senha = vnovasenha
        objusuario.save()
        return render(request, 'alterouSenha.html', { 'usuario': objusuario.usuario })
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

