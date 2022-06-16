from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import  BigtableNomes


class Lista_BigTable_Nomes(ModelAdmin):
    list_display = ('id_principal', 'nome', 'tipo_origem')
    list_per_page = 10
    ordering = ('nome', )
    

admin.site.register(BigtableNomes, Lista_BigTable_Nomes )



