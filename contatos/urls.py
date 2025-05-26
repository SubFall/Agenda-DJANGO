from django.urls import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id_contato>/', views.detalhes_view, name='detail'),

    #CRUD
    path('pesquisa/', views.pesquisa_view, name='pesquisa'),
    path('contato/<int:id_contato>/update/', views.update, name='update'),
    path('contato/<int:id_contato>/delete/', views.delete, name='delete'),
    path('contato/create/', views.create, name='create'),

    #User
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_user, name='login'),
    path('user/logout/', views.logout_user, name='logout'),
    path('user/update/', views.update_user, name='update_user'),
]