"""
Condiciones con operador ternario.
"""

calificacion = 80;
# color = None

# if calificacion >= 70:
#     color = 'Verde'
# else:
#     color = 'Rojo'

# Refactor (con operador ternario)
# En operador ternario, es OBLIGATORIO colocar el else
color = 'verde' if calificacion >= 70 else 'rojo'

print(calificacion, color)

"""
Asignacion de valores mediante operadores lógicos
"""
variable = '' or 0 or [] or True            # Se asigna True

listado = []
nombre = 'Cody'

var = listado or nombre             # Como listado es False (vacio) asignará nombre
print(var)
