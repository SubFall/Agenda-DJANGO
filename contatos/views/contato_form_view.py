from django.shortcuts import render, redirect, get_object_or_404
#from contatos.models import Contato
from .forms import ContatoForm
from django.urls import reverse
from contatos.models import Contato
from django.contrib.auth.decorators import login_required

@login_required(login_url='contatos:login')
def create(request):
    print(f'create: {request.method}')
    form_action = reverse('contatos:create')
    
    if request.method == 'POST':
        #print(request.POST['first_name'])
        form = ContatoForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            print(form.cleaned_data)
            contato = form.save(commit=False)
            contato.owner = request.user
            contato = form.save(commit=True)
            return redirect('contatos:update', id_contato=contato.pk)
        
        return render(
            request,
            'contatos/create.html',
            context
        )

    form = ContatoForm()

    context = {
            #'contatos': contatos,
            'titulo_contato' : 'Contato - ',
            'form': form,
            'titulo': 'Criar Contato'
        }
    return render(
        request,
        'contatos/create.html',
        context
    )

@login_required(login_url='contatos:login')
def update(request, id_contato):
    print(f'update: {request.method}')
    contato = get_object_or_404(Contato, 
                                pk=id_contato, 
                                show=True, 
                                owner=request.user)
    
    form_action = reverse('contatos:update', kwargs={'id_contato':id_contato})
    
    if request.method == 'POST':
        #print(request.POST['first_name'])
        form = ContatoForm(request.POST, request.FILES, instance=contato)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            print(form.cleaned_data)
            contato = form.save()
            return redirect('contatos:update', id_contato=contato.id)
        
        return render(
            request,
            'contatos/create.html',
            context
        )

    form = ContatoForm(instance=contato)

    context = {
            #'contatos': contatos,
            'titulo_contato' : 'Contato - ',
            'form': form,
            'form_action': form_action,
            'titulo': 'Editar Contato'
        }
    return render(
        request,
        'contatos/create.html',
        context
    )

@login_required(login_url='contatos:login')
def delete(request, id_contato):
    print(f'delete: {request.method}')
    contato = get_object_or_404(Contato, 
                                pk=id_contato, 
                                show=True, 
                                owner=request.user)

    confirmacao = request.POST.get('confirmacao', 'no')
    
    #print(confirmacao)

    if confirmacao == 'yes':
        contato.delete()
        return redirect('contatos:index')

    return render(
        request,
        'contatos/detalhes.html',
        {
            'contato': contato,
            'confirmacao': confirmacao
        }
    )
    
    