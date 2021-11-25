# ARHUMENTOS
# Funcion para obtener el promedio de un listado.

# Para indicar que una función puede recibir n cantidad de argumentos se
# indica con un * que serviran para formar una tupla.
# Por convencion de la comunidad, los parametros con * se deben nombrar como
# args
def prom(*args):
    print(args)
    print(type(args))                    # tipo tupla

    return sum(args) / len(args)

# Se pueden combinar argumentos por posicion y argumentos con *
def combinar(a1, a2, a3, *args, p5=11.14):
    print(a1)
    print(a2)
    print(a3)
    print(args)

resultado = prom(5,10,15,20,25)
print(resultado)

combinar('Hola', 23, True, 5, 10, 15.25, False, p5=12.55)