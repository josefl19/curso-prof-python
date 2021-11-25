"""
GENERADORES

Funciones que retornan objetos que se pueden iterar sin que la función finalice.

Son de tipo LAZY ITERATOR, obteniendo los elementos de la función on-demand (cuando sean requeridos)

LAZY ITERATOR:
    - Al ser on-deman no se reserva por completo la memoria a usar (que al final puede no usarse)
    - Genera programas más rápidos.

"""

# No es un generador ya que finaliza.
def pares():
    for n in range(0, 101, 2):
        print(n)

# Generador -> No llevan la palabra return, se usará yield
# Yield permite retornar valores sin que finalice la función pausando la ejecución
def pares_generador():
    for n in range(0, 101, 2):
        yield n                         # Retorna n y suspende su ejecución
        print('Nueva ejecución')

print(pares_generador())            # Imprime un objeto generator

# Iteración del generador.
#for par in pares_generador():
#    print(par)

# Obtner los elementos on-demand
generador = pares_generador()

# Para ir obteniendo los elementos on-demand se usa la función next
print(next(generador))          # Imprime 0 y pausa.
print(next(generador))          # Imprime mensaje y 2.
print(next(generador))          # Imprime mensaje y 4.

print('Imprimimos otra instrucción')        # Se imprime esta línea

print(next(generador))          # Imprime mensaje y 6.

# next puede generar un error en caso de que supere el numero de veces
# llamado al numero de elementos que se retornan.

# Manejo de este error:
while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('Finalizo el generador.')
        break