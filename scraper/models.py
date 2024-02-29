from django.db import models

from django.db import models

class ItemColetado(models.Model):
    codigo = models.CharField(max_length=100)
    descricao_servico = models.TextField()
    unidade = models.CharField(max_length=50)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao_servico
