from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Artigo
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name="autores").exists()


def artigos_view(request):
    artigos = Artigo.objects.select_related("autor").prefetch_related("likes", "comentarios").order_by("-data_criacao")

    return render(request, "artigos/artigos.html", {
        "artigos": artigos,
        "is_autor": is_autor(request.user),
    })


def artigo_detail(request, id):
    artigo = Artigo.objects.select_related("autor").prefetch_related("likes", "comentarios").get(id=id)
    comentarios = artigo.comentarios.select_related("autor").all().order_by("-data_criacao")

    form = ComentarioForm()

    return render(request, "artigos/artigo_detail.html", {
        "artigo": artigo,
        "comentarios": comentarios,
        "form": form,
        "is_autor": is_autor(request.user),
    })


@login_required
def artigo_create(request):
    if not is_autor(request.user):
        return redirect("artigos")

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect("artigos")

    return render(request, "artigos/form.html", {
        "form": form,
        "titulo": "Criar Artigo"
    })


@login_required
def artigo_update(request, id):
    artigo = Artigo.objects.get(id=id)

    if not is_autor(request.user) or artigo.autor != request.user:
        return redirect("artigos")

    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)

    if form.is_valid():
        form.save()
        return redirect("artigo_detail", id=artigo.id)

    return render(request, "artigos/form.html", {
        "form": form,
        "titulo": "Editar Artigo"
    })


@login_required
def artigo_delete(request, id):
    artigo = Artigo.objects.get(id=id)

    if not is_autor(request.user) or artigo.autor != request.user:
        return redirect("artigos")

    if request.method == "POST":
        artigo.delete()
        return redirect("artigos")

    return render(request, "artigos/confirm_delete.html", {
        "objeto": artigo,
        "titulo": "Apagar Artigo"
    })


def artigo_like(request, id):
    artigo = Artigo.objects.get(id=id)

    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)

    return redirect("artigo_detail", id=artigo.id)


@login_required
def comentario_create(request, id):
    artigo = Artigo.objects.get(id=id)
    form = ComentarioForm(request.POST or None)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.artigo = artigo
        comentario.autor = request.user
        comentario.save()

    return redirect("artigo_detail", id=artigo.id)