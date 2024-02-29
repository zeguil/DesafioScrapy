from django.db import models

from django.db import models

class Edital(models.Model):
    descricao_objeto = models.TextField()
    modalidade = models.CharField(max_length=50)
    comprador = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao_objeto

class Itens(models.Model):
    licitacao = models.ForeignKey(Edital, on_delete=models.CASCADE)
    descricao = models.TextField()
    unidade = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)