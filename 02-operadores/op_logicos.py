"""Clase: operadores logicos en Python

Los operadores logicos permiten combinar o invertir condiciones. El resultado
de una condicion suele ser True (verdadero) o False (falso), y se puede usar
para tomar decisiones con if.

AND (and): el resultado es True solo cuando ambas condiciones son True.
OR  (or):  el resultado es True cuando al menos una condicion es True.
NOT (not): invierte el resultado: True pasa a False y False pasa a True.

Tabla de resultados:

    A       B       A and B     A or B
    True    True      True       True
    True    False     False      True
    False   True      False      True
    False   False     False      False

Ejecuta este archivo para ver cada ejemplo impreso en la terminal.
"""

print("=== AND: deben cumplirse las dos condiciones ===")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

print("\n=== OR: basta con que se cumpla una condicion ===")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

print("\n=== NOT: invierte una condicion ===")
print("not True:", not True)
print("not False:", not False)
print("not (2 == 2):", not (2 == 2))

print("\n=== Ejemplo 1: acceso a una pelicula ===")
edad = 20
acompanado_por_adulto = False

# Se permite el acceso si la persona tiene al menos 18 anos o va acompanada.
puede_entrar = edad >= 18 or acompanado_por_adulto
print("Puede entrar:", puede_entrar)

print("\n=== Ejemplo 2: descuento en una tienda ===")
total_compra = 120
es_cliente_frecuente = True

total_compra >= 100 and not es_cliente_frecuente
print("Tiene descuento:", total_compra >= 100 and not es_cliente_frecuente)

# El descuento requiere cumplir ambas condiciones al mismo tiempo.
tiene_descuento = total_compra >= 90 and es_cliente_frecuente
print("Tiene descuento:", tiene_descuento)

print("\n=== Ejemplo 3: comprobar que un campo no este vacio ===")
nombre = ""
nombre_vacio = not nombre
print("El nombre esta vacio:", nombre_vacio)
