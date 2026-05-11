## escola/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('desporto/', views.desporto_view, name="desportos"),
    path('atleta/<int:id>/editar/', views.edita_atleta, name='edita_atleta'),
    path('', views.desporto_view),   #  rota que abre diretamente a página dos cursos
]