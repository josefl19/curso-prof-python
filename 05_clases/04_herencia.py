class Mascota:          # Clase padre
    
    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')

# Herencia
class Perro(Mascota):            # Clase hija
    pass

class Gato(Mascota):
    pass

# duke puede acceder a los metodos de mascota sin ser objeto de esa clase
duke = Perro()
duke.comer()
duke.dormir()

michi = Gato()