# Métodos de STRING
titulo = 'Curso de Python por CodigoFacilito'
titulo2 = 'Curso-de-Python-por-CodigoFacilito'
lista = ['Python', 'Java', 'Go']

# Genera una lista a partir de un String
listado = titulo.split()
listado2 = titulo2.split('-')
print(listado)
print(listado2)

# Se puede indicar el número de elementos que se quiere obtener en la lista
listado3 = titulo.split(' ', 2)
print(listado3)

# Genera un String a parit de una lista. El primer espacio (' ') indica como se separará la cadena
leng_texto = ' '.join(lista)
leng_texto2 = '---'.join(lista)
print(leng_texto)
print(leng_texto2)

# ¡LOS STRINGS SON INMUTABLES!

# Concatenación de String
cadena1 = 'Hola'
cadena2 = 'Mundo!'

concatena = cadena1 + ' ' + cadena2
print(concatena)

mensaje = 'Este es el mensaje: %s %s' %(cadena1, cadena2)
print(mensaje)

mensaje2 = 'Mi mensaje es: {} {}.'.format(cadena1, cadena2)
mensaje3 = 'Mensaje tres: {m1} {m2}.'.format(m1='Adios', m2='Mundo :)')
print(mensaje2)
print(mensaje3)

# BUSQUEDA (SUBSTRING)
# Es sensible a mayusculas y minusculas.
valor = 'Pepe pecas pica papas con un pico de papas'

# Numero de veces que aparece en la cadena dentro de otra
veces = valor.count('papas')
print(veces)

# True/False si la cadena existe dentro del String
print('Pepe' in valor)
print('Pico' not in valor)

# Transforma todo a minusculas
palabra_mayus = 'PEPE'
print(palabra_mayus.lower())

# Verificia si una cadena se encuentra al inicio de una cadena
print(valor.startswith('P'))                # true
print(valor.startswith('Pepe'))             # true
print(valor.startswith('Papa'))             # false

# Verificia si una cadena se encuentra al final de una cadena
print(valor.endswith('r'))                  # false
print(valor.endswith('papas'))              # true
print(valor.endswith('as'))                 # true
