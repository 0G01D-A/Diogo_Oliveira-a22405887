from django.shortcuts import render
from .models import (
    Curso, UC, Professor, Aluno, Competencia,
    Formacao, TFC, Projeto, Tecnologia, Inscricao
)


def home(request):
    return render(request, "portfolio/home.html")


def cursos_view(request):
    cursos = Curso.objects.prefetch_related("ucs").all()
    return render(request, "portfolio/cursos.html", {"cursos": cursos})


def ucs_view(request):
    ucs = UC.objects.select_related("curso").prefetch_related("professores", "projetos", "inscricoes").all()
    return render(request, "portfolio/ucs.html", {"ucs": ucs})


def professores_view(request):
    professores = Professor.objects.select_related("uc", "uc__curso").all()
    return render(request, "portfolio/professores.html", {"professores": professores})


def alunos_view(request):
    alunos = Aluno.objects.prefetch_related("competencias", "projetos", "inscricao").all()
    return render(request, "portfolio/alunos.html", {"alunos": alunos})


def competencias_view(request):
    competencias = Competencia.objects.select_related("aluno").prefetch_related("formacoes").all()
    return render(request, "portfolio/competencias.html", {"competencias": competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related("competencias").all()
    return render(request, "portfolio/formacoes.html", {"formacoes": formacoes})


def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related("tecnologias").all()
    return render(request, "portfolio/tfcs.html", {"tfcs": tfcs})


def projetos_view(request):
    projetos = Projeto.objects.select_related("uc", "uc__curso").prefetch_related("alunos", "tecnologias").all()
    return render(request, "portfolio/projetos.html", {"projetos": projetos})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.select_related("projeto", "tfc").all()
    return render(request, "portfolio/tecnologias.html", {"tecnologias": tecnologias})


def inscricoes_view(request):
    inscricoes = Inscricao.objects.select_related("aluno", "uc", "uc__curso").all()
    return render(request, "portfolio/inscricoes.html", {"inscricoes": inscricoes})