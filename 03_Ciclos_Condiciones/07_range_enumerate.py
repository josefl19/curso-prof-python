# Generar un rango de valores, el ultimo valor del argumento no se incluye
#rango = range(11)           # 0 - 10

# for valor in range(11):
#     print(valor)
# 
# for valor in range(5, 21):      # 5 - 20
#     print(valor)
# 
# for valor in range(2, 21, 2):        # 2 al 21 en saltos de 2            
#     print(valor)


# Enumerate: Permite enumerar los elementos de una colección
numeros = [1, 2, 3, 4, 5]

# retorna un objeto iterable en forma de tupla, el cual contiene un indice
# y el valor.
for indice, numero in enumerate(numeros):
    print(indice, numero)

# Comenzar el inidice en otro numero diferente a 0
for indice, numero in enumerate(numeros, 10):
    print(indice, numero)

