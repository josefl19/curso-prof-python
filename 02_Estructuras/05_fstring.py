"""
FString
Creacion de nuevos String con interpolación
"""

nombre = 'Jose'
apellido = 'Fujarte'

completo = f'Hola {nombre} {apellido}.'
print(completo)

# Alineaciones (n -> numero de espacios a usar)
print(nombre.ljust(10))         # Justificación a la izquierda.
print(nombre.rjust(10))         # Justificación a la derecha.
print(nombre.center(10))        # Centrado

