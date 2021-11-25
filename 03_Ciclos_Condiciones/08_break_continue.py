titulo = 'Curso profesional de Python'

for c in titulo:
    if c == 'P':
        break           # Finaliza de forma indemiate el ciclo

    print(c)

for c in titulo:
    if c == 'o':
        continue           # Salta la ejecución y pasa a la siguiente iteracion

    print(c)