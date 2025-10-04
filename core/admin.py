from django.contrib import admin
from .models import Lote, ProdutoNome, Fornecedor, MovProd
# Register your models here.

class LoteAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Quantidade', 'Nlote', 'Validade']

class ProdutoNomeAdmin(admin.ModelAdmin):
    list_display = ['Nome']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['Emailforn', 'Nome']

class MovprodAdmin(admin.ModelAdmin):
    list_display = ['Tipo', 'Data','Produto', 'Quantidade']

admin.site.register(Lote, LoteAdmin)
admin.site.register(ProdutoNome, ProdutoNomeAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(MovProd, MovprodAdmin)
