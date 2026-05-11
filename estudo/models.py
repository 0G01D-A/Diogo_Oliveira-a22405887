from django.db import models

# Create your models here.


class Desporto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    

class Atleta(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    fotografia = models.ImageField(upload_to='desporto/')
    desportos = models.ManyToManyField(Desporto,related_name='atletas')

    def __str__(self):
        return self.nome + " - " + str(self.idade) + " anos"