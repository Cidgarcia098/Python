"""Guia: operadores de Python

Un operador realiza una accion sobre uno o mas valores. Esta carpeta separa
los principales grupos para aprenderlos paso a paso:

- op_aritmeticos.py: calculos con numeros (+, -, *, /, //, %, **).
- op_comparacion.py: comparaciones que producen True o False (==, <, etc.).
- op_logicos.py: combinacion de condiciones con and, or y not.

Tambien hay operadores de asignacion (=, +=) y de pertenencia (in, not in).
"""

print("=== Asignacion ===")
puntaje = 10
puntaje += 2
print("puntaje despues de += 2:", puntaje)

print("\n=== Pertenencia ===")
lenguajes = ["Python", "JavaScript", "C"]
print("'Python' esta en la lista:", "Python" in lenguajes)
print("'Ruby' no esta en la lista:", "Ruby" not in lenguajes)

print("\n=== Igualdad y asignacion no son lo mismo ===")
valor = 5       # = asigna el valor 5
es_cinco = valor == 5  # == compara dos valores
print("valor:", valor)
print("valor == 5:", es_cinco)

print("\nContinua con op_aritmeticos.py, op_comparacion.py y op_logicos.py.")
