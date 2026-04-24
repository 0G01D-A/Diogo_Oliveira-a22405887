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

    path("projetos/criar/", views.projeto_create, name="projeto_create"),
    path("projetos/<int:id>/editar/", views.projeto_update, name="projeto_update"),
    path("projetos/<int:id>/apagar/", views.projeto_delete, name="projeto_delete"),

    path("tecnologias/criar/", views.tecnologia_create, name="tecnologia_create"),
    path("tecnologias/<int:id>/editar/", views.tecnologia_update, name="tecnologia_update"),
    path("tecnologias/<int:id>/apagar/", views.tecnologia_delete, name="tecnologia_delete"),

    path("competencias/criar/", views.competencia_create, name="competencia_create"),
    path("competencias/<int:id>/editar/", views.competencia_update, name="competencia_update"),
    path("competencias/<int:id>/apagar/", views.competencia_delete, name="competencia_delete"),

    path("formacoes/criar/", views.formacao_create, name="formacao_create"),
    path("formacoes/<int:id>/editar/", views.formacao_update, name="formacao_update"),
    path("formacoes/<int:id>/apagar/", views.formacao_delete, name="formacao_delete"),
]