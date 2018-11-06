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
        #        return render(request, 'eventos/.html', {'post': post})





def listar_eventos(request):
        posts=Evento.objects.all()
        return render(request, 'eventos/listareventos.html', {'posts':posts})

def inicio(request):
    return render(request,'eventos/index.html')


@login_required
def editar_evento(request, pk):
    post = get_object_or_404(Evento, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
           # formulario.save()
            return redirect('detalle_evento', pk=post.pk)
    else:
        form = EventoForm(instance=post)
        return render(request, 'eventos/editar_evento.html', {'form': form})

@login_required
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

@login_required
def evento_remove(request, pk):
    post = get_object_or_404(Evento, pk=pk)
    post.delete()
    return redirect('listar_eventos')




def listar_personas(request):
        posts=Persona.objects.all()
        return render(request, 'eventos/listarpersonas.html', {'posts':posts})

def detalle_persona(request, pk):
        post = get_object_or_404(Persona, pk=pk)
        return render(request, 'eventos/detalle_personas.html', {'post': post})

@login_required
def persona_nueva(request):
    if request.method == "POST":
        formulario = PersonaForm(request.POST,request.FILES)
        if formulario.is_valid():
            add=formulario.save(commit=False)
            add.save()
            formulario.save_m2m()
            #form.save_m2m()
            return redirect('detalle_persona', pk=add.pk)    
    else:

        formulario = PersonaForm()

    return render(request, 'eventos/ingreso_persona.html', {'formulario': formulario})

@login_required
def editar_persona(request, pk):
    prod = get_object_or_404(Persona, pk=pk)

    if request.method == "POST":

        form = PersonaForm(request.POST,request.FILES, instance=prod)
        if form.is_valid():
            edit_persona=form.save(commit=False)
            form.save_m2m()
            edit_persona.save()
            return redirect('detalle_persona', pk=edit_persona.pk)

            #evento = Evento.objects.create(nombre=formulario.cleaned_data['nombre'], fecha = formulario.cleaned_data['fecha'])
            

           #messages.add_message(request, messages.SUCCESS, 'Evento Guardado Exitosamente')

            #evento = Evento.objects.create(nombre=form.cleaned_data['nombre'], fecha = form.cleaned_data['fecha'])

    else:
        form = PersonaForm(instance=prod)
    return render(request, 'eventos/editar_persona.html', {'form': form})

@login_required
def persona_remove(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    post.delete()
    return redirect('listar_personas')
    

        