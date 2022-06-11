from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from . models import  DrugbankNome, AnvisaPrincipioativo, AnvisaNome, BigtableNomes, AnvisaNomePrincipioativo, DrugbankAnvisa, DrugbankInteracao


class Lista_AnvisaNome(ModelAdmin):
    list_display = ('id', 'nomeproduto')
    list_per_page = 10
    ordering = ('id', )
    search_fields = ('nomeproduto', )
    

class Lista_DrugBank_Nome(ModelAdmin):
    list_display = ('drugbank_id', 'name')
    list_per_page = 10
    ordering = ('drugbank_id', )

class Lista_Anvisa_PrincipioAtivo(ModelAdmin):
    list_display = ('id_pativo', 'nome_pativo', 'translated_pativo')
    list_per_page = 10
    ordering = ('id_pativo', )

class Lista_BigTable_Nomes(ModelAdmin):
    list_display = ('id_principal', 'nome', 'tipo_origem')
    list_per_page = 10
    ordering = ('nome', )
    
class Lista_AnvisaNomePrincipioativo(ModelAdmin):
    list_display = ('idproduto', 'idprincipio')
    list_per_page = 10
    
class Lista_DrugbankAnvisa(ModelAdmin):
    list_display = ('drugbank', 'id_pativo', 'matchingvalue')
    list_per_page = 10
    ordering = ('drugbank', )

class Lista_DrugbankAnvisa(ModelAdmin):
    list_display = ('drugbank', 'id_pativo', 'matchingvalue')
    list_per_page = 10
    ordering = ('drugbank', )

class Lista_DrugbankInteracao(ModelAdmin):
    list_display = ('drugbank_id1', 'drugbank_id2')
    list_per_page = 10



admin.site.register(DrugbankNome, Lista_DrugBank_Nome)
admin.site.register(AnvisaPrincipioativo, Lista_Anvisa_PrincipioAtivo )
admin.site.register(AnvisaNome, Lista_AnvisaNome )
admin.site.register(BigtableNomes, Lista_BigTable_Nomes )
admin.site.register(AnvisaNomePrincipioativo, Lista_AnvisaNomePrincipioativo )
admin.site.register(DrugbankAnvisa, Lista_DrugbankAnvisa )
admin.site.register(DrugbankInteracao, Lista_DrugbankInteracao )



