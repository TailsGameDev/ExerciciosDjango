from django.urls import path, include
from .views import helloApp, loginSubmit, login, alterarSenha, criarUsuario

urlpatterns = [
    path('', helloApp, name='helloApp'),
    path('login', login, name='login'),
    path('loginSubmit', loginSubmit, name='loginSubmit'),
    path('alterarSenha', alterarSenha, name='alterarSenha'),
    path('criarUsuario', criarUsuario, name='criarUsuario'),
]