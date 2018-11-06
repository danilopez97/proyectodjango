from django.shortcuts import render,get_object_or_404
#librería para manejar el envío de mensajes
from django.contrib import messages
from .forms import EventoForm,PersonaForm
from eventos.models import Persona, Evento
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

# Create your views here.
def detalle_evento(request, pk):
        post = get_object_or_404(Evento, pk=pk)
        return render(request, 'eventos/detalle_eventos.html', {'post': post})


def listar_eventos(request):
        posts=Evento.objects.all()
        return render(request, 'eventos/listareventos.html', {'posts':posts})

def inicio(request):
    return render(request,'eventos/index.html')









def editar_evento(request, pk):
    post = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detalle_evento', pk=post.pk)
    else:
        form = EventoForm(instance=post)
        return render(request, 'eventos/editar_evento.html', {'form': form})

def evento_nuevo(request):
        if request.method == "POST":
            form = EventoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('detalle_evento', pk=post.pk)
        else:
            form = EventoForm()
        return render(request, 'eventos/ingreso_evento.html', {'form': form})


def evento_remove(request, pk):
    post = get_object_or_404(Evento, pk=pk)
    post.delete()
    return redirect('listar_eventos')
    

        