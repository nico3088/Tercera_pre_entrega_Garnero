from django import forms
from .models import Estudiantes, Profesor, Tutor, Cursos

class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre', 'apellido', 'edad', 'ciudad', 'email']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'edad', 'ciudad', 'email']

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nombre', 'apellido', 'edad', 'ciudad', 'email']

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'duracion', 'horario', 'Inscriptos']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Buscar', max_length=100)