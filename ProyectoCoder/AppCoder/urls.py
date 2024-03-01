from django.urls import path, include
from AppCoder.views import *
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('crear_entregable/', crear_entregable, name='crear_entregable'),
    path('estudiante/', crear_estudiante, name='crear_estudiante'),
    path('ver_cursos/', ver_cursos, name='ver_cursos'),
    path('ver_estudiantes/', ver_estudiantes, name='ver_estudiantes'),
    path('ver_profesores/', ver_profesores, name='ver_profesores'),
    path('ver_entregables/', ver_entregables, name='ver_entregables'),
    path('', inicio, name='inicio')
]
