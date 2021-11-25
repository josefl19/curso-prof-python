# Forma para definir e inicialzar objetos mediante un método

class Usuario:

    # Método (los métodos tiene un parametro). Self indica que hace referencia a si mismo.
    def inicializar(self, username, password):
        # Atributos de objeto.
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()

# No se pasa nada como parametro self ya que representa al objeto en si.
user1.inicializar('Jose', '123')
user2.inicializar('Raul', '345')

# Imprimir los atributos del objeto.
print(user1.__dict__)
print(user2.__dict__)