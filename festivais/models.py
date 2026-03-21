from django.db import models

# Create your models here.
class Festival(models.Model):
    nome = models.CharField(max_length=100)
    bilhetes = models.IntegerField()


    def __str__(self):
        return f"{self.nome}: {self.bilhetes} vendidos."
