from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Artigo, Comentario


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "data_criacao")
    search_fields = ("titulo", "texto", "autor__username")
    list_filter = ("data_criacao", "autor")


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("artigo", "autor", "data_criacao")
    search_fields = ("texto", "autor__username", "artigo__titulo")
    list_filter = ("data_criacao",)


admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)