from django.shortcuts import render
from hashlib import sha256
import os

def _1_webServiceUI(request):
    return render(request, '_1_webServiceUI.html')

def _1_resumoCriptografico(request):
    arquivoBinario = request.FILES['file']
    #arquivoBinario = open(os.path.realpath('lsec\\views.py'), 'rb')
    textoArquivo = arquivoBinario.read()
    resumoCriptografico = sha256(textoArquivo)
    return render(request,'resumoCriptografico.html', { 'resumoCriptografico': resumoCriptografico.hexdigest })