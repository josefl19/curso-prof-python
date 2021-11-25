def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):

        if cantidad <= balance:        
            return balance - cantidad
        else:
            return None

    print(id(cantidad))
    print(id(balance))

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

resultado_dep = operacion(100, 30)              # Deposito
resultado_ret = operacion(10, 30, 'retiro')

print(resultado_dep)
print(resultado_ret)