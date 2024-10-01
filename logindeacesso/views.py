from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')

        if User.objects.filter(username=usuario).exists():
            return HttpResponse("Já existe um usuário!")

        User.objects.create_user(username=usuario, email=email, password=senha)
        return HttpResponse("Usuário cadastrado com sucesso!")

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            return HttpResponse("Autenticado!")
        else:
            return HttpResponse("Usuário ou senha inválido!")
