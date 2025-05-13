from django.shortcuts import render, redirect
from contatos.models import Contato
from django.db.models import Q

def pesquisa_view(request):

    _get = request.GET.get('q', '').strip()

    print('teste', _get)

    if _get == '':
        return redirect('contatos:index')

    contatos = Contato.objects\
        .filter(show=True)\
        .filter(Q(first_name__icontains=_get) |
                Q(last_name__icontains=_get) |
                Q(phone__icontains=_get) |
                Q(email__icontains=_get) 
        )\
        .order_by('-id')

    print(contatos.query)

    context = {
        'contatos': contatos,
        'titulo_contato' : 'Contato - '
    }
    return render(
        request,
        'contatos/index.html',
        context
    )