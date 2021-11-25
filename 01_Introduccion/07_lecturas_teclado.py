# Lectura de valores por teclado
lectura = input('Nombre: ')
print(lectura)
print(type(lectura))                # input -> tipo str

# Convertir el valor ingresado a otro tipo (parseo)
numero = int(input('Numero: '))
print(type(numero))

flotante = float(input('Flotante: '))
print(type(flotante))

booleano = input('Si o no? ')
booleano = booleano == 'Si'
print(booleano)
