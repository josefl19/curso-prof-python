# Scope
animal = 'León' # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    global animal           # Modifica el valor de una variable global
    animal = 'Ballena'

    # animal = 'Ballena' # Variable Local

    tipo = 'Mamifero' # Variable Local

    print(animal)
    print(id(animal))
    
imprimir_animal()

print(animal)
print(id(animal))