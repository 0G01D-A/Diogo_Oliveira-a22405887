from django.contrib import admin
from .models import Escola

# Register your models here.
class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome","localidade",)
    ordering = ("nome","quantidade_alunos",)
    search_fields = ("nome",)

admin.site.register(Escola,EscolaAdmin)
