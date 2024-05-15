from django import forms
from .models import Lote, ProdutoNome

class LoteModelForm(forms.ModelForm):

    class Meta:
        model = Lote
        fields = "__all__"