from django.shortcuts import render
from .models import Contato

def home(request):
    return render(request, 'website/index.html')

def contato(request):
    mensagem = ''
    tipo = 0
    if request.method == 'POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['endereco'] = request.POST.get('endereco')
            contato['bairro'] = request.POST.get('bairro')
            contato['cidade'] = request.POST.get('cidade')
            contato['mensagem'] = request.POST.get('mensagem')
            contato['novidades'] = True if request.POST.get('novidades') == 'on' else False 

            Contato.objects.create(**contato)    
        except Exception as e:
            mensagem = str(e)
            tipo = 1
        else:
            mensagem = 'Mensagem enviada com sucesso!' 

    return render(request, 'website/contato.html', {'mensagem': mensagem, 'tipo': tipo})    

def servicos(request):
    return render(request, 'website/servicos.html')