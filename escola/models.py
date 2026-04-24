from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()


    def __str__(self):
        return f"{self.nome}"
        # Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nome}"
    
# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='cursos/')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    alunos = models.ManyToManyField(Aluno, related_name='cursos')


    def __str__(self):
        return f"{self.nome}"
    


