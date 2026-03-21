from django.contrib import admin

from .models import Loja

# Register your models here.
class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome","quantidade_empregados",)
    ordering = ("nome","quantidade_empregados",)
    search_fields = ("nome",)

admin.site.register(Loja,LojaAdmin)
