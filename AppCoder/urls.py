from django.urls import path
from .views import *

urlpatterns = [
        path("inicio/", inicio, name="Inicio"),
        path("cursos/", ver_cursos),
        path("profes/", ver_profes),
        path("entregas/", ver_entregables),
        path("crear_estudiante/", crear_estudiantes, name="crearEstudiante"),
        path("crear_curso/", crear_cursos, name="crearCursos"),
        path("crear_profe/", crear_profes, name="crearProfes"),
        path("buscar_profe/", buscar_profes, name="BuscarProfes"),
        path("resu_profe/", resultado_profes, name="ResultadoProfes"),
]