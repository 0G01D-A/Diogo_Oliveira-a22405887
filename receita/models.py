from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=100)
    quantidades_ingredientes = models.IntegerField()


    def __str__(self):
        return f"{self.nome}: {self.quantidades_ingredientes} ingredientes utilizados nesta receita."
