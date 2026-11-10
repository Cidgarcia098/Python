"""Clase: convertir entradas del usuario a numeros

input() siempre devuelve texto. Para calcular con la entrada hay que
convertirla, por ejemplo con int() para enteros o float() para decimales.
Escribe el decimal con punto (por ejemplo, 3.5).
"""

try:
    texto_entero = input("Escribe un numero entero: ").strip()
    numero_entero = int(texto_entero)

    texto_decimal = input("Escribe un numero, puede tener decimales: ").strip()
    numero_decimal = float(texto_decimal)
except ValueError:
    print("Entrada no valida: revisa el formato de los numeros.")
else:
    print(f"El entero multiplicado por 2 es {numero_entero * 2}.")
    print(f"El decimal multiplicado por 2 es {numero_decimal * 2}.")

    # Multiplicar texto por 2 lo repite; no realiza un calculo numerico.
    print("El texto del entero repetido dos veces es:", texto_entero * 2)
