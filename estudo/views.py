from django.shortcuts import render,redirect
from .models import Atleta,Desporto
from .forms import AtletaForm

# Create your views here.
def desporto_view(request):
    desportos = (Desporto.objects
               .all())
    
    atletas = (Atleta.objects
               .prefetch_related('desportos')
               .all())
    
    tenis = Desporto.objects.get(nome="Ténis")

    menores = tenis.atletas.filter(idade__lt=18)


    ordenar_idade = atletas.order_by('idade')
    

    return render(request, 'estudo/desporto.html', {'desportos':desportos,'atletas':atletas,'menores':menores,'tenis':tenis,'ordenar_idade':ordenar_idade})

def edita_atleta(request, id):
    atleta = Atleta.objects.get(id=id)

    form = AtletaForm(request.POST or None,request.FILES or None, instance=atleta)

    if form.is_valid():
        form.save()
        return redirect("desportos")

    return render(request, 'estudo/edita_atleta.html', {
        'form': form,
        'atleta': atleta,
    })