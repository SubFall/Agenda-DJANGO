from django.shortcuts import render
from contatos.models import Contato

def index_view(request):

    contatos = Contato.objects.all()

    context = {
        'contatos': contatos
    }
    return render(
        request,
        'contatos/index.html',
        context
    )