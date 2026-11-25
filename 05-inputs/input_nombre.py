"""Clase: recibir texto con input()

input() muestra un mensaje, espera a que la persona escriba y devuelve lo
escrito como str. strip() quita espacios al principio y al final.
"""

nombre = input("Escribe tu nombre: ").strip()

if nombre:
    print(f"Hola, {nombre}. Bienvenido al curso de Python.")
else:
    print("No escribiste un nombre.")

print("Tipo de dato que devuelve input():", type(nombre).__name__)
