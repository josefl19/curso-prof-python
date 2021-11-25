"""
DICCIONARIOS

Son mutables (añadir, modificar o eliminar).
No se rigen por indices, sino por la relación llave-valor.
No se permiten las llaves duplicadas, en caso de existir se sobreescribe el valor de esta.
"""

# Definicion/creación
diccionario = {}
diccionario2 = dict()

# { llave: valor asociado }
diccionario = {"nombre": 'Jose'}
diccionario = {"nombre": 'José', "edad": 23}

# Agregar nueva llave-valor
diccionario2['usuario'] = 'Pepe'

# Actualizar valor mediante llave, si no existe la crea.
diccionario2['usuario'] = 'Javier'

# Obtener le valor mediante una llave
print(diccionario2['usuario'])

# Tamaño de un diccionario con el uso de len()

# Métodos
dicc = {'Jose': 1, 'Jessamyn': 2, 'Elsy': 3}

# Obtener las llaves
dicc_key = dicc.keys()          # puede convertirse a una tupla
print(dicc_key)

# Obtener los valores del diccionario, siempre y cuando exista
# Con in podemos verificar si esa llave existe en el diccionario.
dicc_values = dicc.values()     # puede convertirse a una tupla
print(dicc_values)

# Obtener los itemes del diccionario
dicc_items = dicc.items();      # puede convertirse a una tupla
print(dicc_items)

# Recorrido del diccionario
for key, value in dicc.items():
    print(key, value)

# Eliminar un elemento en un diccionario
# Por llave
del dicc['Elsy']
print(dicc)

# Uso de pop, retorna el valor del item eliminado
valor = dicc.pop('Jessamyn')
print(valor)
print(dicc)

#Eliminar todos los elementos
dicc.clear()
print(dicc)

# Obtencion de un valor mediante su llave
# Si no existe la llave se puede establecer uno por default para evitar el error
usuario = {
    'nombre': 'Jose Fujarte',
    'edad': 23,
    'signo': 'Acuario'
}

calificacion = usuario.get('calificacion', [])      # asigna una lista vacia en caso de no existir (u otro tipo de dato)
if calificacion:
    for cal in calificacion:
        print(cal)

# Obtener el valor de una llave, si no existe se añadira al diccionario
valor = usuario.setdefault('carrera', 'Ing. Sistemas')
print(usuario)

