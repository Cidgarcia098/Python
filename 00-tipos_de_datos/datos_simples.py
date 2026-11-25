"""Clase 1: tipos de datos simples

Un tipo de dato describe que clase de valor contiene una variable y que
operaciones tienen sentido para ese valor. Python identifica el tipo
automaticamente; podemos consultarlo con type().

Tipos basicos:
- str: texto entre comillas.
- int: numero entero.
- float: numero decimal (en el codigo se escribe con punto).
- complex: numero complejo, con la parte imaginaria indicada por j.
- bool: valor logico True o False (con mayuscula inicial).
- NoneType: ausencia intencional de un valor, representada por None.
"""

nombre = "Lucia"
edad = 20
altura = 1.68
numero_complejo = 2 + 3j
es_estudiante = True
resultado_pendiente = None

datos = [
    ("nombre", nombre),
    ("edad", edad),
    ("altura", altura),
    ("numero complejo", numero_complejo),
    ("es estudiante", es_estudiante),
    ("resultado pendiente", resultado_pendiente),
]

for etiqueta, valor in datos:
    print(f"{etiqueta}: {valor!r} -> {type(valor).__name__}")

# bool es un tipo propio, aunque en Python tambien se comporta como un
# subtipo de int. Para aprender, conviene tratarlo como un valor logico.
print("\nUna condicion de comparacion produce un bool:", edad >= 18)
