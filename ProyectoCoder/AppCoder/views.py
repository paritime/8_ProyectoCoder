from django.shortcuts import render
from django.shortcuts import HttpResponse
from AppCoder.models import Curso, Estudiantes, Entregable
from AppCoder.forms import Entregable_form
import datetime


# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def ver_cursos(request):
    return render(request, 'ver_cursos.html')


def ver_estudiantes(request):
    return render(request, 'ver_estudiantes.html')


def ver_profesores(request):
    return render(request, 'ver_profesores.html')


def ver_entregables(request):
    return render(request, 'ver_entregables.html')


def crear_curso(request):
    if request.method == 'POST':
        curso_nuevo = Curso(
            nombre=request.POST['nombre'], comision=request.POST['comision'])
        curso_nuevo.save()
        print('Se guardo el curso')
        return render(request, 'inicio.html')
    return render(request, 'crear_curso.html')


def crear_entregable(request):
    if request.method == 'POST':
        formulario = Entregable_form(request.POST)
        validation = formulario.is_valid()
        print(validation)
        if formulario.is_valid():
            info_dicc = formulario.cleaned_data
            print(info_dicc)
            entregable_nueva = Entregable(nombre=info_dicc['nombre'],
                                          fechaEntrega=info_dicc['fechaEntrega'],
                                          entregado=info_dicc['entregado'])
            entregable_nueva.save()
            return render(request, 'inicio.html')
    else:
        print('no se guardo el entregable')
        formulario = Entregable_form()

    return render(request, 'crear_entregable.html', {'form': Entregable_form})


def crear_estudiante(request):
    estudiante_1 = Estudiantes(
        nombre='Diego',
        apellido='Ramos',
        email='parisarc@gmail.com',
        edad=35)

    estudiante_2 = Estudiantes(
        nombre='Django',
        apellido='Pythons',
        email='django@gmail.com',
        edad=40)

    estudiante_1.save()
    estudiante_2.save()

    return HttpResponse(f'Hemos creado a los estudiantes: {estudiante_1.nombre} y {estudiante_2.nombre} ')
