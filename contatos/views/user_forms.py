from django.shortcuts import render, redirect
from .forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('contatos:login')

    return render(
        request,
        'contatos/register.html',
        {
            'form': form,
            'titulo': 'Criar Usuário'
        }         
    )

def login_user(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('contatos:index')
        messages.error(request, 'Usuário ou senha inválidos.')

    return render(
        request,
        'contatos/login.html',
        {
            'form': form 
        }         
    )

@login_required(login_url='contatos:login')
def logout_user(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso.')
    return redirect('contatos:login')

@login_required(login_url='contatos:login')
def update_user(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('contatos:update_user')

    return render(
        request,
        'contatos/register.html',
        {
            'form': form,
            'titulo': 'Atualizar Usuário'
        }         
    )