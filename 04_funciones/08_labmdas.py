# lambda <parámetros> : <Cuerpo de la función>

funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(10))

"""
sin_parametros = lambda : True
paremtros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwargs: len(args) + len(kwargs)
"""

# Se puede asignar a una variable una función
def cent_to_farh(grados):
    return grados * 1.8 + 32

mi_funcion = cent_to_farh       # Se puede asignar una función a una variable
print(type(mi_funcion))
print(mi_funcion(10))