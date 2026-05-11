from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import MagicLinkToken
from .forms import RegistoForm
import secrets


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user:
            login(request, user)
            return redirect("portfolio_home")

        return render(request, "accounts/login.html", {
            "mensagem": "Credenciais inválidas."
        })

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("portfolio_home")


def registo_view(request):
    form = RegistoForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        grupo, created = Group.objects.get_or_create(name="autores")
        user.groups.add(grupo)

        login(request, user)

        return redirect("portfolio_home")

    return render(request, "accounts/registo.html", {
        "form": form
    })

def magic_login_request(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            token = secrets.token_urlsafe(32)

            MagicLinkToken.objects.create(
                user=user,
                token=token
            )

            host = "https://fluffy-spoon-97xqr9g4rqww3x69j-8000.app.github.dev"
            link = f"{host}/accounts/magic-login/{token}/"

            send_mail(
                subject="Link mágico de acesso ao Portfólio",
                message=f"Clica neste link para entrar no portfólio: {link}",
                from_email=None,
                recipient_list=[email],
            )

        return render(request, "accounts/login.html", {
            "mensagem": "Se o email existir, foi enviado um link de acesso."
        })

    return redirect("login")

def magic_login_confirm(request, token):
    magic_token = MagicLinkToken.objects.get(token=token)

    if magic_token.usado or magic_token.expirado():
        return render(request, "accounts/magic_login_invalid.html")

    magic_token.usado = True
    magic_token.save()

    login(request, magic_token.user)

    return redirect("portfolio_home")