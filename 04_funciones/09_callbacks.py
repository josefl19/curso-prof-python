# Función labmda para obtener el promedio.
promedio = lambda *args : sum(args) / len(args)

# Función labmda para determinar si una calificación es aprobatoria
aprobatorio = lambda calificacion : calificacion >= 7

"""
Los callbacks son ideales para cuando se trabaja con un programa modular, ya que
perimite que sea más facil la actualización del código al solo cambiar la función
que se va a ejecutar por la correspondiente.

Ej. La función mostrat_mensaje puede inicialmente recibir la función aprobatorio
pero despues segun las necesidades puede que la forma de determinar si una calificación
es aprobatoria cambie, por ejemplo, la definida como es_aprobatorios. Solo se deberia
cambiar la función que se llama en la función sin necesidad de cambiar otras líneas.
"""

# Nueva función para determinar si una calificación es aprobatoria.
def es_aprobatorio(calificacion):
    return calificacion >= 90

# Función que llama a otras funciones como argumentos.
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}.')
    else:
        print('No aprobaste la materia.')

# Ejecucuión de la función.
mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)
mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 7, 7)