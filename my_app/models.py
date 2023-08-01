from django.db import models

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey('Cursos', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Tutor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey('Cursos', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField()
    horario = models.CharField(max_length=100)
    inscriptos = models.ManyToManyField(Estudiantes)

    def __str__(self):
        return self.nombre