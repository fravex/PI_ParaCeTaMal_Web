from django.contrib import admin


from . models import BigtableNomes

class BigTableNomesAdmin(admin.ModelAdmin):
    ordering = ['nome']
    search_fields = ['nome']
    list_display = ('nome', 'tipo_origem')


admin.site.register(BigtableNomes,BigTableNomesAdmin )