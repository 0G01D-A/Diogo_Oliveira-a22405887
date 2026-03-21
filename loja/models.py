from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_empregados = models.IntegerField()


    def __str__(self):
        return f"{self.nome}: {self.quantidade_empregados} empregados."
