from django.contrib import admin
from .models import Receita

# Register your models here.
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome","quantidades_ingredientes",)
    ordering = ("nome","quantidades_ingredientes",)
    search_fields = ("nome",)

admin.site.register(Receita,ReceitaAdmin)
