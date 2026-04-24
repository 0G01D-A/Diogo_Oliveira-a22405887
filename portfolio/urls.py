from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="portfolio_home"),
    path("cursos/", views.cursos_view, name="portfolio_cursos"),
    path("ucs/", views.ucs_view, name="portfolio_ucs"),
    path("professores/", views.professores_view, name="portfolio_professores"),
    path("alunos/", views.alunos_view, name="portfolio_alunos"),
    path("competencias/", views.competencias_view, name="portfolio_competencias"),
    path("formacoes/", views.formacoes_view, name="portfolio_formacoes"),
    path("tfcs/", views.tfcs_view, name="portfolio_tfcs"),
    path("projetos/", views.projetos_view, name="portfolio_projetos"),
    path("tecnologias/", views.tecnologias_view, name="portfolio_tecnologias"),
    path("inscricoes/", views.inscricoes_view, name="portfolio_inscricoes"),
]