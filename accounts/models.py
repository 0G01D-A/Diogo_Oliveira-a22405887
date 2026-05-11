from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import secrets


class MagicLinkToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="magic_tokens")
    token = models.CharField(max_length=120, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    def expirado(self):
        return timezone.now() > self.criado_em + timedelta(minutes=15)

    def __str__(self):
        return f"Magic link de {self.user.username}"