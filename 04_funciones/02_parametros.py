# El nombre de las funciones debe serguir el snakecase

# Funcion de suma con párametros
def suma(n1, n2):
    resultado = n1 + n2
    print(resultado)

# Lectura de variables
n1 = int(input('Primer numero entero: '))
n2 = int(input('Segundo numero entero: '))

# Llamada a la función
suma(n1, n2)

# Los parámetros pueden ser opcionales
# Los parametros que tengan valor por default siempre deben ir a la derecha
# Si se llegara a indicar un parametro que tiene valor, se sobreescribe.
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)        # ** para indicar que se eleva a cierta potencia

area_c = area_circulo(10)

# Si se indica el nombre del parametro, no importa la posición
area_c2 = area_circulo(radio=5, pi=14.22)

print(area_c)
print(area_c2)
