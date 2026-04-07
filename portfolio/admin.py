from django.contrib import admin
from .models import (
    Curso,
    UC,
    Professor,
    Aluno,
    Competencia,
    Formacao,
    TFC,
    Projeto,
    Tecnologia,
    Inscricao
)


class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "duracao", "ects_total")
    ordering = ("nome",)
    search_fields = ("nome",)


class UCAdmin(admin.ModelAdmin):
    list_display = ("nome", "semestre", "ects", "curso")
    ordering = ("semestre", "nome")
    search_fields = ("nome",)
    list_filter = ("semestre", "curso")


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "uc")
    ordering = ("nome",)
    search_fields = ("nome", "email")
    list_filter = ("uc",)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "data_nascimento")
    ordering = ("nome",)
    search_fields = ("nome", "email")


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel", "aluno")
    ordering = ("nome",)
    search_fields = ("nome",)
    list_filter = ("nivel",)


class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao", "data_inicio", "data_fim")
    ordering = ("-data_inicio",)
    search_fields = ("nome", "instituicao")


class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "licenciatura", "rating", "autores", "orientadores")
    ordering = ("titulo", "rating")
    search_fields = ("titulo", "licenciatura", "autores", "orientadores", "areas")
    list_filter = ("licenciatura", "rating")


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "uc", "data_inicio", "nota_final")
    ordering = ("-data_inicio",)
    search_fields = ("nome",)
    list_filter = ("uc",)


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "projeto", "tfc")
    ordering = ("nome",)
    search_fields = ("nome", "categoria")
    list_filter = ("categoria",)


class InscricaoAdmin(admin.ModelAdmin):
    list_display = ("aluno", "uc", "nota_final", "data_inscricao")
    ordering = ("-data_inscricao",)
    search_fields = ("aluno__nome", "uc__nome")
    list_filter = ("uc", "data_inscricao")


admin.site.register(Curso, CursoAdmin)
admin.site.register(UC, UCAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Inscricao, InscricaoAdmin)