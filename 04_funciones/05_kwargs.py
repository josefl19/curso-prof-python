# A diferencia de *args que genera una tupla, 
# kwargs hara el uso de diccionarios.

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10,20,30], jose=[10,14,19])

# Se puede combinar con *args
