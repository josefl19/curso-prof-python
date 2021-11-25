e = 'e'             # Global

def func_principal():
    # Variable local. Tiene un scope superior y pueden ser usadas en
    # otros bloques de funciones definidas dentro ("Globales dentro de la función")
    a = 'a'         # Local, Scope superiro
    b = 'b'         # Local, Scope superiro

    def func_anidada():
        c = 'c'         # Local. Solo se usa en func_anidada.

        # Cambair el valor de una variable de scope superior
        nonlocal b
        b = 'Cambio de valor'

        print(a)    
        print(b)
        print(e)
    
    func_anidada()
    #print(c)            # ERROR. No se puede acceder a esta variable porque ya ha sido destruida.

func_principal()

"""
============================================================
Las funciones son ciudadanos de primera clase, por lo cual pueden retornar funciones

CLOSURE
Función que puede generar de forma dinámica a otra función y esta funcipon nueva,
puede acceder a la variables locales aunque la primera haya finalizado.

"""

def saludar(username):
    mensaje = f'Hola {username}' # Variable Local

    def mostrar_mensaje(): # Anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)       # respues almacena la función.

username = 'Eduardo'                # No realiza ningun cambio.

respuesta()         # Uso de las variables que fueron creadas localmente
respuesta()
respuesta()