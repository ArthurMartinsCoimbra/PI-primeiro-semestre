from django.contrib import admin
from .models import Lote, ProdutoNome
# Register your models here.

class LoteAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Quantidade', 'Nlote', 'Validade']

class ProdutoNomeAdmin(admin.ModelAdmin):
    list_display = ['Nome']

admin.site.register(Lote, LoteAdmin)
admin.site.register(ProdutoNome, ProdutoNomeAdmin)