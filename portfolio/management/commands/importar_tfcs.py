import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from portfolio.models import TFC


class Command(BaseCommand):
    help = "Importa os TFCs a partir do ficheiro JSON"

    def handle(self, *args, **kwargs):
        caminho = os.path.join(settings.BASE_DIR, "data", "tfcs_2024_2025_V2.json")

        if not os.path.exists(caminho):
            self.stdout.write(self.style.ERROR(f"Ficheiro não encontrado: {caminho}"))
            return

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        contador = 0

        for item in dados:
            titulo = item.get("titulo", "").strip()

            if not titulo:
                continue

            TFC.objects.update_or_create(
                titulo=titulo,
                licenciatura=item.get("licenciatura", "").strip(),
                defaults={
                    "autores": item.get("autores", "").strip(),
                    "orientadores": item.get("orientadores", "").strip(),
                    "sumario": item.get("sumario", "").strip(),
                    "pdf": item.get("pdf", "").strip(),
                    "imagem": item.get("imagem", "").strip(),
                    "palavras_chave": item.get("palavras_chave", "").strip(),
                    "areas": item.get("areas", "").strip(),
                    "tecnologias_usadas": item.get("tecnologias_usadas", "").strip(),
                    "rating": item.get("rating", 0),
                }
            )

            contador += 1

        self.stdout.write(self.style.SUCCESS(f"{contador} TFC(s) importado(s) com sucesso."))