from django.shortcuts import render
from contatos.models import Contato

def index_view(request):

    contatos = Contato.objects.filter(show=True).order_by('-id')

    context = {
        'contatos': contatos,
        'titulo_contato' : 'Contato - '
    }
    return render(
        request,
        'contatos/index.html',
        context
    )