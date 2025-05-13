from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contatos.models import Contato

def detalhes_view(request, id_contato):

    #contatos = Contato.objects.filter(id=id_contato).first()

    #if contatos is None:
    #    raise Http404()
    contatos = get_object_or_404(Contato, id=id_contato, show=True)

    print(contatos)
    


    context = {
        'contato': contatos,
        'titulo_contato' : f'{contatos.first_name} - '
    }

    print(id_contato)
    return render(
        request,
        'contatos/detalhes.html',
        context
    )