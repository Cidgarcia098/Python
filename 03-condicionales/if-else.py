"""Clase: tomar una decision con if y else

if ejecuta un bloque cuando su condicion es verdadera. else ejecuta la
alternativa cuando esa condicion es falsa. else no lleva condicion y es
opcional si no se necesita una accion alternativa.

La indentacion define que instrucciones pertenecen a cada bloque.
"""

edad = 17
print("Edad:", edad)

if edad >= 18:
    print("Tienes 18 años o más en este ejemplo.")
else:
    print("Tienes menos de 18 años.")

# Una comparacion produce True o False, y ese resultado decide el bloque.
numero = 8
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")

# Cambia edad o numero y vuelve a ejecutar el archivo para probar los otros
# caminos. Los ejemplos usan valores fijos para ser faciles de repetir.
