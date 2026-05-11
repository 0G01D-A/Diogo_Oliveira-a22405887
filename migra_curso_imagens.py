import os
import django
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.core.files import File
from portfolio.models import Tecnologia


migrados = 0
nao_encontrados = 0
sem_logo = 0
ja_cloud = 0

for obj in Tecnologia.objects.all():
    if not obj.logo or not obj.logo.name:
        sem_logo += 1
        print(f"Sem logo: {obj}")
        continue

    try:
        local_path = obj.logo.path
    except Exception:
        ja_cloud += 1
        print(f"Provavelmente já está na cloud ou sem path local: {obj} -> {obj.logo.name}")
        continue

    if not os.path.exists(local_path):
        nao_encontrados += 1
        print(f"Ficheiro não encontrado: {local_path}")
        continue

    nome_ficheiro = os.path.basename(local_path)

    with open(local_path, "rb") as f:
        obj.logo.save(
            nome_ficheiro,
            File(f),
            save=True
        )

    migrados += 1
    print(f"Migrado para Cloudinary: {obj} -> {nome_ficheiro}")


print("\nResumo:")
print(f"Migrados: {migrados}")
print(f"Sem logo: {sem_logo}")
print(f"Ficheiros não encontrados: {nao_encontrados}")
print(f"Já na cloud / sem path local: {ja_cloud}")