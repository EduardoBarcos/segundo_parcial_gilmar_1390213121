from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Recurso
from .forms import RecursoForm

@login_required
def listar_recursos(request):
    recursos = Recurso.objects.all()
    return render(request, 'Tarea/listar_recursos.html', {'recursos': recursos})

@permission_required('Tarea.add_recurso', raise_exception=True)
def crear_recurso(request):
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            recurso = form.save(commit=False)
            recurso.propietario = request.user
            recurso.save()
            return redirect('listar_recursos')
    else:
        form = RecursoForm()
    return render(request, 'Tarea/crear_recurso.html', {'form': form})

@permission_required('Tarea.change_recurso', raise_exception=True)
def modificar_recurso(request, id):
    recurso = get_object_or_404(Recurso, id=id)
    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('listar_recursos')
    else:
        form = RecursoForm(instance=recurso)
    return render(request, 'Tarea/modificar_recurso.html', {'form': form})

@permission_required('Tarea.delete_recurso', raise_exception=True)
def eliminar_recurso(request, id):
    recurso = get_object_or_404(Recurso, id=id)
    if request.method == 'POST':
        recurso.delete()
        return redirect('listar_recursos')
    return render(request, 'Tarea/eliminar_recurso.html', {'recurso': recurso})
