from django.urls import path, include
from .views import helloApp, loginSubmit, login, usarServicos, criarUsuario
from .views import getUsuarios

urlpatterns = [
    path('', helloApp, name='helloApp'),
    path('login', login, name='login'),
    path('loginSubmit', loginSubmit, name='loginSubmit'),
    path('usarServicos', usarServicos, name='usarServicos'),
    path('criarUsuario', criarUsuario, name='criarUsuario'),
    path('getUsuarios', getUsuarios, name='getUsuarios')
]