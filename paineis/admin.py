from django.contrib import admin
from .models import Vendas, Revistas

class ListaVendas(admin.ModelAdmin):
    list_display = ("id", "ano", "vendas")
    list_display_links = ("id","ano")
    search_fields = ("ano",)
    # list_filter = ("categoria",)
    # list_editable = ("publicada",)
    list_per_page = 10

class ListaRevistas(admin.ModelAdmin):
    list_display = ("id", "ano","volume","tema","secao","autor","titulo","genero_textual","palavra_chave1","palavra_chave2","palavra_chave3","sexo_autor")
    list_display_links = ("id","ano")
    search_fields = ("ano", "volume", 'autor', 'palavra_chave1', 'palavra_chave2', 'palavra_chave3')
    list_filter = ("ano", "volume", 'autor', "genero_textual",)
    # list_editable = ("publicada",)
    list_per_page = 25
    # Escolha um dos dois: list_filter_horizontal ou list_filter_vertical
    list_filter_horizontal = ("ano", "volume", 'autor', "genero_textual",)  # Filtros horizontais
    #list_filter_vertical = ("ano", "volume", 'autor', "genero_textual",)  # Filtros verticais

admin.site.register(Vendas, ListaVendas)
admin.site.register(Revistas, ListaRevistas)