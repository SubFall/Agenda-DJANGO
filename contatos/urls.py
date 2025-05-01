from django.urls import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('', views.index_view, name='index'),
]
