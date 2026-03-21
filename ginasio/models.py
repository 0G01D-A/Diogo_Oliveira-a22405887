from django.db import models


# Create your models here.
class Ginasio(models.Model):
    nome = models.CharField(max_length=100)
    alunos_inscritos = models.IntegerField()


    def __str__(self):
        return f"{self.nome}: {self.alunos_inscritos} alunos inscritos."
