# Algunos métodos de las listas:
numeros = [2,14,1,22,19,53,66,101,7]

# Oreden de mayor a menor
numeros.sort()
print(numeros)

# Ordenar de mayot a menor
numeros.sort(reverse=True)
print(numeros)

# Obtener el valor MIN de una lista
minimo = min(numeros)
print(minimo)

# Obtener el máximo
maximo = max(numeros)
print(maximo)

# Saber si un elemento se encuentra (o no) en la lista
print(10 in numeros)                # false
print(101 in numeros)               # true
print(101 not in numeros)           # false

# Saber el index que ocupa un elemento en una lista
print(numeros.index(19))

# Matrices
col_a = [1, 2]
col_b = [10, 20]

matriz = [col_a, col_b]
print(matriz)
