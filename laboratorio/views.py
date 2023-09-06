from django.shortcuts import render
from .forms import LaboratorioForm
from .models import Laboratorio
from django.http import HttpResponseRedirect


# Create your views here.


def v_list(request):

    context = {
        'labos': Laboratorio.objects.all()
    }
    return render(request, 'list.html', context)

def v_create(request):
    context = {
        'formulario': LaboratorioForm()
    }
    return render(request, 'create.html', context)

def v_update(request, laboratorio_id):
    lab = Laboratorio.objects.get(id = laboratorio_id)
    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = LaboratorioForm(datos, instance = lab)
        if formeditar.is_valid():
            formeditar.save()
        return HttpResponseRedirect("/")
    else:
        context = {
            'formedicion': LaboratorioForm(instance = lab)
        }
        return render(request, 'update.html', context)

def v_delete(request, laboratorio_id):
    context = {}
    return render(request, 'delete.html', context)