"""
DECORADORES

Reduce lineas de codigo, codigo mas legible, testeable y más mantenible.
Extiende funcionalidades a una función sin tener que modificarla.

Funcion que toma como valor de entrada una función y retorna una función.
(Al menos 3 funciones: input, output y la principal (decorador)):

a - Funcion principal (Docorador)
b - Función de decorar
c - Función decorada 

a(b) -> c

"""

# Estructura base:
def func_a(func_b):
    
    def func_c():
        print('Hola desde func_c')       
        func_b()                         # Ejecuta el mensaje de saludar()
        print('Adiós desde func_c')

    return func_c

@func_a
def saludar():
    print('Homa mundo, desde saludar')

saludar()

@func_a
def suma():
    print(10+50)

suma()