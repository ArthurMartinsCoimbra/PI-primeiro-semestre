from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
# Create your models here.






class Fornecedor(models.Model):
    Emailforn = models.EmailField(primary_key=True)
    Nome = models.CharField('Nome', max_length=100)
    def __str__(self):
        return self.Nome


class ProdutoNome(models.Model):
    Nome = models.CharField('Nome', max_length=100, primary_key=True)
    Formail1 = models.EmailField('Email1', null=True, blank= True)
    Formail2 = models.EmailField('Email2', null=True, blank= True)
    Formail3 = models.EmailField('Email3', null=True, blank= True)
    Formail4 = models.EmailField('Email4', null=True, blank= True)
    Formail5 = models.EmailField('Email5', null=True, blank= True)
    def __str__(self):
        return self.Nome


class Lote(models.Model):
    Nome = models.CharField('Nome',max_length=40, null = True, blank = True)
    Quantidade = models.DecimalField('Quantidade no Lote',max_digits=8, decimal_places=0)
    Nlote = models.CharField('Numero do Lote',max_length=40, primary_key=True)
    Validade = models.DateField('Validade', auto_now=False, auto_now_add=False)
    Usuario = models.ForeignKey(User, null=True, blank= True, on_delete=models.DO_NOTHING, related_name="usuarios_lote")
    '''def __str__(self):
        return self.Nome'''
    


class MovProd(models.Model):
    TIPO_TIPOS = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    
    Tipo = models.CharField(max_length=10, choices=TIPO_TIPOS)
    Data = models.DateField()
    Produto = models.ForeignKey(ProdutoNome, on_delete=models.CASCADE)
    Quantidade = models.PositiveBigIntegerField(default=0)

    def save(self, *args, **kwargs):
        
        if self.pk is None:
            existente = MovProd.objects.filter(
                Produto = self.Produto,
                Data = self.Data,
                Tipo = self.Tipo
            ).first()
            if existente:
                existente.Quantidade = F('Quantidade') + self.Quantidade
                existente.save(update_fields = ["Quantidade"])
                return
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.Produto} - {self.Tipo} - {self.Data} - ({self.Quantidade})"
