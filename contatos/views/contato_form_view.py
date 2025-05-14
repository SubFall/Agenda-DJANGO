from django.shortcuts import render
from contatos.models import Contato

def create(request):


    context = {
        #'contatos': contatos,
        'titulo_contato' : 'Contato - ',
    }
    return render(
        request,
        'contatos/create.html',
        context
    )