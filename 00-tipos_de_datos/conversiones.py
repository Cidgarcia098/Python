"""Clase 3: consultar y convertir tipos

type(valor) nos permite consultar el tipo de un valor. Las funciones int(),
float() y str() intentan convertir un valor a otro tipo. La conversion puede
fallar si el texto no tiene un formato valido (por ejemplo, int("tres")).

Importante: int() elimina la parte decimal hacia cero; no redondea.
"""

precio_texto = "12.50"
precio = float(precio_texto)
cantidad_texto = "3"
cantidad = int(cantidad_texto)

print("Texto:", precio_texto, "->", type(precio_texto).__name__)
print("Precio convertido:", precio, "->", type(precio).__name__)
print("Cantidad convertida:", cantidad, "->", type(cantidad).__name__)
print("Total:", precio * cantidad)

numero = 8
mensaje = "El numero es " + str(numero)
print("\nConversion a texto:", mensaje)

decimal = 4.9
print("int(4.9) elimina decimales, no redondea:", int(decimal))
print("round(4.9) redondea:", round(decimal))

# bool() considera vacios valores como "", 0 y None como False. El texto
# "False", en cambio, no esta vacio y por eso bool("False") es True.
print("\nbool(''):", bool(""))
print("bool('False'):", bool("False"))
