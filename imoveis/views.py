from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from imoveis.models import Imovel, Inquilino
from .forms import ImovelForm


# Página Inicial
def index(request):
    return render(request, 'imoveis/index.html')


# Listagem de Imóveis
def list_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imoveis/list_imoveis.html', {'imoveis': imoveis})


def editar_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)

    if request.method == 'POST':
        form = ImovelForm(request, instance=imovel)
        form.save()
        return redirect('list_imoveis')
    else:
        form = ImovelForm(instance=imovel)
    return render(request, 'imoveis/editar_imovel.html', {'form': form})


def excluir_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)

    if request.method == 'POST':
        imovel.delete()
        return redirect('lista_imoveis')
    return render(request, 'imoveis/excluir_imoveis.html', {'imovel': imovel})


def list_inquilinos(request):
    inquilinos = Inquilino.objects.all()
    return render(request, 'imoveis/list_inquilinos.html', {'inquilinos': inquilinos})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'imoveis/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'imoveis/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
