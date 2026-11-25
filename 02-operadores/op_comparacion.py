"""Clase: operadores de comparacion

Las comparaciones enfrentan dos valores y producen un resultado booleano:
True o False. == comprueba igualdad; =, en cambio, asigna un valor.
"""

edad = 18
edad_minima = 18

print("Igual (==):", edad == edad_minima)
print("Distinto (!=):", edad != edad_minima)
print("Mayor (>):", edad > edad_minima)
print("Menor (<):", edad < edad_minima)
print("Mayor o igual (>=):", edad >= edad_minima)
print("Menor o igual (<=):", edad <= edad_minima)

# Las comparaciones se pueden guardar y luego usar en una condicion.
tiene_edad_minima = edad >= edad_minima
print("\nTipo del resultado:", type(tiene_edad_minima).__name__)

# Python permite encadenar comparaciones para comprobar un rango.
temperatura = 22
esta_templado = 18 <= temperatura <= 25
print(f"{temperatura} esta entre 18 y 25:", esta_templado)

# La igualdad de texto distingue mayusculas de minusculas.
print("\n'Python' == 'python':", "Python" == "python")
