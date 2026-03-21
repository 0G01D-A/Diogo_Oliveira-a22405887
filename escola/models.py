from django.db import models

# Create your models here.
class Escola(models.Model):
    nome = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    quantidade_alunos = models.IntegerField()


    def __str__(self):
        return f"A {self.nome} situa-se em {self.localidade} e tem {self.quantidade_alunos}"