from django.contrib import admin

from contatos import models

@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'id', 'phone',

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',