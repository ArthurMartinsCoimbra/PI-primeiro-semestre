from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Lote(models.Model):
    Nome = models.CharField('Nome do produto',max_length=100)
    Quantidade = models.DecimalField('Quantidade no Lote',max_digits=8, decimal_places=0)
    Nlote = models.CharField('Numero do Lote',max_length=40, primary_key=True)
    Validade = models.DateField('Validade', auto_now=False, auto_now_add=False)
    Usuario = models.ForeignKey(User, null=True, blank= True, on_delete=models.DO_NOTHING, related_name="usuarios_lote")
    def __str__(self) -> str:
        return self.Nome + ' ' + self.Nlote
    
class ProdutoNome(models.Model):
    Nome = models.CharField('Nome', max_length=100, primary_key=True)