"""Clase: elegir entre varias alternativas con if, elif y else

Python evalua las condiciones de arriba hacia abajo. Ejecuta solo el primer
bloque cuya condicion sea verdadera; si ninguna coincide, ejecuta else.
elif significa "si no, si". Puede haber varios elif y el else es opcional.

El orden importa. En una clasificacion por rangos, las condiciones deben
separar claramente los intervalos para que cada valor tenga un resultado.
"""

puntaje = 76
print("Puntaje:", puntaje)

if puntaje >= 90:
    calificacion = "Excelente"
elif puntaje >= 75:
    calificacion = "Muy bien"
elif puntaje >= 60:
    calificacion = "Aprobado"
else:
    calificacion = "Hay que seguir practicando"

print("Resultado:", calificacion)

# Ejemplos de limites: cada valor pertenece a una sola categoria.
for puntaje_de_prueba in (95, 90, 75, 60, 59):
    if puntaje_de_prueba >= 90:
        resultado = "Excelente"
    elif puntaje_de_prueba >= 75:
        resultado = "Muy bien"
    elif puntaje_de_prueba >= 60:
        resultado = "Aprobado"
    else:
        resultado = "Hay que seguir practicando"
    print(f"{puntaje_de_prueba}: {resultado}")

# A diferencia de una cadena if-elif, dos if independientes pueden ejecutarse
# ambos si sus condiciones son verdaderas.
temperatura = 28
if temperatura > 20:
    print("\nHace mas de 20 grados.")
if temperatura > 25:
    print("Tambien hace mas de 25 grados.")
