from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()
    ects_total = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class UC(models.Model):
    nome = models.CharField(max_length=100)
    ects = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="ucs")

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    uc = models.ForeignKey(UC, on_delete=models.CASCADE, related_name="professores")

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=50)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="competencias")

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    instituicao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    nome = models.CharField(max_length=150)

    competencias = models.ManyToManyField(Competencia, related_name="formacoes")

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.TextField(blank=True)
    orientadores = models.TextField(blank=True)
    licenciatura = models.CharField(max_length=255, blank=True)
    sumario = models.TextField(blank=True)
    pdf = models.URLField(blank=True)
    imagem = models.URLField(blank=True)
    palavras_chave = models.TextField(blank=True)
    areas = models.TextField(blank=True)
    tecnologias_usadas = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    nota_final = models.DecimalField(max_digits=4, decimal_places=2)

    alunos = models.ManyToManyField(Aluno, related_name="projetos")
    uc = models.ForeignKey(UC, on_delete=models.CASCADE, related_name="projetos")

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    categoria = models.CharField(max_length=100)
    website = models.URLField()
    logo = models.ImageField(upload_to="tecnologias_logos/", null=True, blank=True)
    nome = models.CharField(max_length=100)

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="tecnologias")
    tfc = models.ForeignKey(TFC, on_delete=models.CASCADE, related_name="tecnologias")

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    nota_final = models.DecimalField(max_digits=4, decimal_places=2)
    data_inscricao = models.DateField()

    uc = models.ForeignKey(UC, on_delete=models.CASCADE, related_name="inscricoes")
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, related_name="inscricao")

    def __str__(self):
        return f"{self.aluno.nome} - {self.uc.nome}"