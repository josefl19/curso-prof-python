# Nombre de clase en CamelCase y singular
# pass -> evita tener un bloque vacio y que genere un error

""""
Atributos de clase -> Pertencen a la clase.

Atributos de instancia -> Pertenecen al objeto de una clase
"""
class Prueba:
    pass            # Se definen métodos y clases

# cody = Prueba()
# print(cody)

class Usuario:
    # Atributos de clase
    username = 'Default'
    email = ''

# Acceso y uso de los atributos de la clase.
# Usuario.username = 'Jose'
# Usuario.email = 'correo@mail.com'
# print(Usuario.username)

# Creación de objeto.
# __dict__ -> ver atributos del objeto

usuario1 = Usuario()
"""
Pasos que se realizan en Python:
1. Verifica que el atributo existe dentro del obejto.
2. Verfica que el atributo existe dentro de la clase (si no hay 1, usa este) -> Lectura
3. Si no es 1 o 2, entonces error.
"""

print(usuario1.username)        # Retorna el atributo de la clase.
print(usuario1.__dict__)

# Otro objeto al que se le agregan sus atributos.
usuario2 = Usuario()
# Atributo de instancia
usuario2.username = 'Cody'      # El objeto usuario 2 tiene un nombre que no es el atributo de objeto
usuario2.password = '1234'      # Crea el atributo password para el obejto usuario2
print(usuario2.username)
print(usuario2.__dict__)