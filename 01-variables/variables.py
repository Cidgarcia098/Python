"""Clase: variables y asignacion

Una variable es un nombre asociado a un valor. El signo = asigna o actualiza
el valor; no significa "es igual a" como en matematicas.

Buenas practicas:
- Usa nombres descriptivos en snake_case, como precio_total.
- Los nombres distinguen mayusculas de minusculas: edad y Edad son distintos.
- Un nombre comienza con una letra o _, no con un numero.
- Evita palabras reservadas como if, for o class como nombres.
"""

nombre = "Lucia"
edad = 20
print(f"Hola, {nombre}. Tienes {edad} años.")

# Una asignacion nueva reemplaza el valor anterior.
puntaje = 10
print("\nPuntaje inicial:", puntaje)
puntaje = 15
print("Puntaje actualizado:", puntaje)

# Las asignaciones aumentadas usan el valor actual de la variable.
puntaje += 5
print("Despues de puntaje += 5:", puntaje)

# La expresion de la derecha se calcula antes de guardar el resultado.
nombre_completo = nombre + " Garcia"
print("\nNombre completo:", nombre_completo)

# Una f-string inserta valores dentro de un texto y permite expresiones.
precio = 12.5
cantidad = 3
print(f"Compra: {cantidad} unidades a ${precio:.2f} cada una.")
print(f"Total: ${precio * cantidad:.2f}")

# input() devuelve texto (str), incluso cuando se escriben digitos.
# Para trabajar con numeros, convierte la entrada con int() o float().
print("\nEl tipo de nombre es:", type(nombre).__name__)
