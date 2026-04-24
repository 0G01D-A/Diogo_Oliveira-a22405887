from django.shortcuts import render,redirect
from .models import (
    Curso, UC, Professor, Aluno, Competencia,
    Formacao, TFC, Projeto, Tecnologia, Inscricao,
)

from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm

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


def projeto_create(request):
    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_projetos")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Criar Projeto"
    })


def projeto_update(request, id):
    projeto = Projeto.objects.get(id=id)

    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return redirect("portfolio_projetos")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Editar Projeto"
    })


def projeto_delete(request, id):
    projeto = Projeto.objects.get(id=id)

    if request.method == "POST":
        projeto.delete()
        return redirect("portfolio_projetos")

    return render(request, "portfolio/confirm_delete.html", {
        "objeto": projeto,
        "titulo": "Apagar Projeto"
    })

def tecnologia_create(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_tecnologias")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Criar Tecnologia"
    })


def tecnologia_update(request, id):
    tecnologia = Tecnologia.objects.get(id=id)

    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)

    if form.is_valid():
        form.save()
        return redirect("portfolio_tecnologias")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Editar Tecnologia"
    })


def tecnologia_delete(request, id):
    tecnologia = Tecnologia.objects.get(id=id)

    if request.method == "POST":
        tecnologia.delete()
        return redirect("portfolio_tecnologias")

    return render(request, "portfolio/confirm_delete.html", {
        "objeto": tecnologia,
        "titulo": "Apagar Tecnologia"
    })


def competencia_create(request):
    form = CompetenciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_competencias")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Criar Competência"
    })


def competencia_update(request, id):
    competencia = Competencia.objects.get(id=id)

    form = CompetenciaForm(request.POST or None, instance=competencia)

    if form.is_valid():
        form.save()
        return redirect("portfolio_competencias")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Editar Competência"
    })


def competencia_delete(request, id):
    competencia = Competencia.objects.get(id=id)

    if request.method == "POST":
        competencia.delete()
        return redirect("portfolio_competencias")

    return render(request, "portfolio/confirm_delete.html", {
        "objeto": competencia,
        "titulo": "Apagar Competência"
    })


def formacao_create(request):
    form = FormacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("portfolio_formacoes")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Criar Formação"
    })


def formacao_update(request, id):
    formacao = Formacao.objects.get(id=id)

    form = FormacaoForm(request.POST or None, instance=formacao)

    if form.is_valid():
        form.save()
        return redirect("portfolio_formacoes")

    return render(request, "portfolio/form.html", {
        "form": form,
        "titulo": "Editar Formação"
    })


def formacao_delete(request, id):
    formacao = Formacao.objects.get(id=id)

    if request.method == "POST":
        formacao.delete()
        return redirect("portfolio_formacoes")

    return render(request, "portfolio/confirm_delete.html", {
        "objeto": formacao,
        "titulo": "Apagar Formação"
    })
