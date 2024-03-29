from django.db import models

# Create your models here.

class Lote(models.Model):
    Nome = models.CharField('Nome do produto',max_length=100)
    Quantidade = models.DecimalField('Quantidade no Lote',max_digits=8, decimal_places=0)
    Nlote = models.CharField('Numero do Lote',max_length=40, primary_key=True)
    Validade = models.DateField('Validade', auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.Nome + ' ' + self.Nlote