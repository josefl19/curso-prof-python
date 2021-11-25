class Circulo:

    pi = 3.141592           #Atributo de clase

    @classmethod                    # Decorador, para indicar que el método es de clase y no de instancia
    def area(cls, radio):           # Método de clase. Cls hace ref. a la clase
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)