"""
TUPLAS
Son INMUTABLES (no se les puede agregar, eliminar o cambiar sus elementos)
"""
tupla = ()
tupla_2 = ('String', 1, 3.14, True, [2,4,6], (3,6,9))

# Acceso a un valor
print(tupla_2[5])


# Generar una tupla a partir de una lista y una lista a partir de una tupla
lista = [1,3,5,9,12]
tupla = (2,4,6,8,10)

nueva_tupla = tuple(lista)
print(nueva_tupla)

nueva_lista = list(tupla)
print(nueva_lista)

# DESCOMPRIMIR TUPLA
# Asigna los valores de la tupla en las variables según el orden.
numeros = (1,2,3,4,5,6,7,8)
#uno, dos, tres, cuatro, cinco = numeros
#print(uno, dos, tres, cuatro, cinco)

# Almacenar el resto de valores de una tupla
# * -> lista
# _ -> ignorar
uno, dos, tres, *resto = numeros
print(uno)
print(dos)
print(tres)
print(resto)
print(type(resto))

""" 
COMPRIMIR UNA TUPLA (ZIP)
zip() -> combina lo elementos en pares de listas/tuplas en una sola
"""
tupla = (1,2,3,4,5)
lista = [10,20,30,40,50]

nuevo = zip(tupla, lista)           # retorna un tipo zip (se puede convertir usando tuple())
print(tuple(nuevo))

# Pueden ser de un tipo, combinado y de mas de dos valores.
# Si alguna tupla/lista tiene más elementos que otros, el restante se ignora.