"""Clase: tomar decisiones con if, elif y else

Estas estructuras permiten que un programa elija qué instrucciones ejecutar
según se cumplan o no unas condiciones.

La forma general es:

    if primera_condicion:
        # Se ejecuta si la primera condición es verdadera.
    elif segunda_condicion:
        # Se ejecuta si la primera fue falsa y la segunda es verdadera.
    else:
        # Se ejecuta si ninguna condición anterior fue verdadera.

Python revisa las condiciones de arriba hacia abajo y ejecuta solo el primer
bloque que corresponda. Por eso, el orden importa: conviene escribir primero
los casos más específicos y después los más generales. `else` es opcional y
no lleva una condición.

Ejemplo con edades:

    edad = 15
    if edad < 18:
        print("Menor de edad")
    elif edad < 65:
        print("Adulto")
    else:
        print("Adulto mayor")

Con edad 15 se imprime "Menor de edad". Con edad 30 se imprime "Adulto":
la primera condición es falsa y la segunda verdadera. Con edad 70 se imprime
"Adulto mayor", porque ambas condiciones anteriores son falsas.

Ahora probaremos dos decisiones relacionadas con un presupuesto: una cadena
`if-elif-else` para clasificar el ingreso y otra para comparar los gastos.
"""

ingreso_mensual = float(input("Ingrese su ingreso mensual: "))
gasto_mensual = float(input("Ingrese su gasto mensual: "))

# Cada elif se considera solo si las condiciones anteriores fueron falsas.
if ingreso_mensual < 500:
    print("Ingreso bajo.")
elif ingreso_mensual < 1000:
    print("Ingreso medio.")
elif ingreso_mensual < 2000:
    print("Ingreso alto.")
else:
    print("Ingreso muy alto.")

# Esta segunda cadena toma una decisión distinta: compara gastos e ingresos.
if gasto_mensual > ingreso_mensual:
    print("Tus gastos superan tus ingresos.")
elif gasto_mensual == ingreso_mensual:
    print("Gastaste todo tu ingreso.")
else:
    print("Te quedó dinero después de los gastos.")
