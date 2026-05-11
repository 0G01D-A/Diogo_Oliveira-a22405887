from django.urls import path
from . import views

urlpatterns = [
    path("", views.artigos_view, name="artigos"),
    path("<int:id>/", views.artigo_detail, name="artigo_detail"),
    path("criar/", views.artigo_create, name="artigo_create"),
    path("<int:id>/editar/", views.artigo_update, name="artigo_update"),
    path("<int:id>/apagar/", views.artigo_delete, name="artigo_delete"),
    path("<int:id>/like/", views.artigo_like, name="artigo_like"),
    path("<int:id>/comentario/", views.comentario_create, name="comentario_create"),
]