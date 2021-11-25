calificacion = 55

# Condicion normal
if calificacion == 100:
    print('Excelente calificación')
else:
    print('Que mala calificación')

# Elif
if calificacion == 100:                                 # 100
    print('Excelente calificación')
elif calificacion > 80 and calificacion < 100:          # 81 - 99
    print('Buen trabajo. Sigue así.')
elif calificacion >= 70 and calificacion <= 80:         # 70 - 80
    print('Bien hecho, aunque puedes mejorar')
else:
    print('No aprobado. Pon mayor esfuerszo.')          # <70
