# El nombre de las funciones debe serguir el snakecase

# Funcion de suma con párametros con retorno de un valor
def suma(n1, n2):
    return n1 + n2

# Funcion con parémetros y retorno de más de un valor (en forma de tupla)
def resta(n1, n2):
    return n1 - n2, 'Retorno de la resta de dos numeros'        # Retorna una tupla

# Lectura de variables
n1 = int(input('Primer numero entero: '))
n2 = int(input('Segundo numero entero: '))

# Llamada a la función
res = suma(n1, n2)
print(res)

# Llamada a la función de resta, se deben desempaquetar los valores
res_resta, mensaje = resta(n1, n2)
print('Resta: ', res_resta)
print(mensaje)
