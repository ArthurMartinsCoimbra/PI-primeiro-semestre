from django.contrib import admin
from .models import Lote
# Register your models here.

class LoteAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Quantidade', 'Nlote', 'Validade']

admin.site.register(Lote, LoteAdmin)