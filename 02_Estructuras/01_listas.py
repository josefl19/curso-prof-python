# LISTAS

# Formas de definicion:
lista_uno = []
lista_dos = list()

# TIP: Almacenar preferentemente un solo tipo de dato en una lista (si es posible)

lista_lenguajes = ['Java', 'Python', 'C', 'C++', 'C#', 'Javascript', 'PHP']
# Acceso a un elemento de la lista:
print(lista_lenguajes[0])
print(lista_lenguajes[-1])           # -1 accede al último valor

# Actualizar el valor de un elemento de la lista
lista_lenguajes[5] = 'JavaScript'
print(lista_lenguajes)

"""
Creacion de sublistas (una lista a partir de otra)
    [inicio:fin]            El valor del fin no se añade como elemento a la lista.
    [inicio:fin:salto]      Saltos entre los valores
"""
sub1 = lista_lenguajes[0:3]             # De Java a C
sub2 = lista_lenguajes[0:]              # De Java a PHP
sub3 = lista_lenguajes[3:]              # De C++ a PHP
sub4 = lista_lenguajes[:4]              # De Java a C++
sub5 = lista_lenguajes[1:6:2]           # De Python a PHP en saltos de 2 -> (Python,C++,Javascript)
sub6 = lista_lenguajes[2:5:3]           # De C a Javascript en saltos de 3 -> (C)
sub7 = lista_lenguajes[::]              # Todos los elementos
sub8 = lista_lenguajes[::-1]            # Invertir la lista

#print(sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sep='\n')

# Añadir elementos a una lista
lista_lenguajes.append('Rust')
print(lista_lenguajes)

lista_lenguajes.insert(3, 'HTML')           # Insertar en un index
lista_lenguajes.insert(6, 'R')
print(lista_lenguajes)

# Longitud de una lista
print(len(lista_lenguajes))

# Eliminar elementos de una lista
lista_lenguajes.remove('HTML')          # Por valor del elemento
print(lista_lenguajes)

del lista_lenguajes[2]                  # Por index
print(lista_lenguajes)

#lista_lenguajes.clear()                   # Toda la lista
#print(lista_lenguajes)

# Añadir elementos de otra lista en una lista.
lenguajes_dos = ['Scala', 'Ruby', 'Go']
lista_lenguajes.extend(lenguajes_dos)
print(lista_lenguajes)

