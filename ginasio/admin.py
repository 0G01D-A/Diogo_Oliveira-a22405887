from django.contrib import admin
from .models import Ginasio

# Register your models here.
class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome","alunos_inscritos",)
    ordering = ("nome","alunos_inscritos",)
    search_fields = ("nome",)

admin.site.register(Ginasio,GinasioAdmin)