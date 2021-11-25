# Forma para definir e inicialzar objetos sin método creados y al momento en el que crean.

class Usuario:
    # Se usa el método init para indicar atributos desde la creación del obejto
    # SE pueden usar variables por default
    def __init__(self, username='', password='') -> None:
        self.username = username
        self.password = password
        print('Creación de usuario')

# Creacion del objeto e inicialización de sus atributos
user1 = Usuario('Jose', '123')
user2 = Usuario('Raul', '345')
user3 = Usuario()

# Imprimir los atributos del objeto.
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)