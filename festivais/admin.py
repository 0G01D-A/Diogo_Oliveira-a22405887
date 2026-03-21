from django.contrib import admin
from .models import Festival

# Register your models here.
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome","bilhetes",)
    ordering = ("nome","bilhetes",)
    search_fields = ("nome",)

admin.site.register(Festival,FestivalAdmin)
