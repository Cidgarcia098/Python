"""Clase: operadores logicos

Se usan para combinar o invertir condiciones:
- and es True cuando todas las condiciones son True.
- or es True cuando al menos una condicion es True.
- not invierte una condicion: True pasa a False y viceversa.

Al combinar comparaciones (que producen bool), el resultado tambien es bool.
"""

print("=== Tabla de verdad ===")
casos = [(True, True), (True, False), (False, True), (False, False)]
for primera, segunda in casos:
    print(
        f"A={primera:<5} B={segunda:<5} "
        f"A and B={primera and segunda:<5} A or B={primera or segunda}"
    )

print("\n=== NOT ===")
print("not True:", not True)
print("not False:", not False)

print("\n=== Ejemplo AND: descuento ===")
total_compra = 120
es_cliente_frecuente = True
tiene_descuento = total_compra >= 100 and es_cliente_frecuente
print("Cumple el minimo y es cliente frecuente:", tiene_descuento)

print("\n=== Ejemplo OR: acceso a una pelicula ===")
edad = 16
acompanado_por_adulto = True
puede_entrar = edad >= 18 or acompanado_por_adulto
print("Puede entrar:", puede_entrar)

print("\n=== Ejemplo NOT: campo opcional ===")
comentario = ""
no_escribio_comentario = not comentario
print("No escribio un comentario:", no_escribio_comentario)

# En condiciones, los valores vacios (por ejemplo "", 0 y []) se consideran
# falsos; los no vacios suelen considerarse verdaderos.
print("\nbool('texto'):", bool("texto"))
print("bool(''):", bool(""))
