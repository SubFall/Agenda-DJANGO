from django.shortcuts import render
from contatos.models import Contato
from django.core.paginator import Paginator

def index_view(request):

    contatos = Contato.objects.filter(show=True).order_by('-id')
    paginacao = Paginator(contatos, 10)

    page_number = request.GET.get('page')
    page_obj = paginacao.get_page(page_number)

    context = {
        #'contatos': contatos,
        'titulo_contato' : 'Contato - ',
        'page_obj': page_obj
    }
    return render(
        request,
        'contatos/index.html',
        context
    )