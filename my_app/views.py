from django.shortcuts import render, redirect
from .models import Cursos
from .forms import EstudiantesForm, ProfesorForm, TutorForm, CursosForm, BusquedaForm

def cursos_view(request):
    cursos = Cursos.objects.all()
    
    if request.method == 'POST':
        cursos_form = CursosForm(request.POST)
        if cursos_form.is_valid():
            cursos_form.save()
            return redirect('cursos')
        
        busqueda_form = BusquedaForm(request.POST)
        if busqueda_form.is_valid():
            busqueda = busqueda_form.cleaned_data['busqueda']

    else:
        cursos_form = CursosForm()
        busqueda_form = BusquedaForm()

    return render(request, 'my_app/cursos.html', {'cursos': cursos, 'cursos_form': cursos_form, 'busqueda_form': busqueda_form})