from django.urls import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id_contato>/', views.detalhes_view, name='detail'),

    #CRUD
    path('pesquisa/', views.pesquisa_view, name='pesquisa'),
    path('contato/create/', views.create, name='create')
]
