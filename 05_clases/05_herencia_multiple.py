class Animal():
    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')


class Mascota(Animal):          # Clase padre
    pass

class Can:
    def ladran(self):
        print('Los canes ladran')

# Herencia
class Perro(Mascota, Can):            # Clase hija
    pass

# duke puede acceder a los metodos de mascota sin ser objeto de esa clase
duke = Perro()
duke.comer()
duke.dormir()
duke.ladran()