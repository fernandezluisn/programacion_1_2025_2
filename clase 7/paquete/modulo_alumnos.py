SALUDO_ALUMNOS = "Hola estudiantes"

def calcular_promedio(total: float,
                      cantidad_materias: int) -> float:

    '''
    '''

    return total / cantidad_materias

def controlar_asistencia(cantidad_clases: int,
                         cantidad_faltas: int)-> str:
    
    porcentaje_faltas = cantidad_faltas / cantidad_clases

    if porcentaje_faltas > 0.25:
        situacion_alumno = "libre"
    else:
        situacion_alumno = "regular"

    return situacion_alumno