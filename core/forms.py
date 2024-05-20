from django import forms
from .models import Lote, ProdutoNome

class LoteModelForm(forms.ModelForm):

    class Meta:
        model = Lote
        fields = ['Nome', 'Quantidade', 'Validade']
        widgets = {
            'validade' : forms.DateInput(attrs={'type':'date'})
        }