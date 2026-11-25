"""Clase: operadores aritmeticos

Estos operadores realizan calculos. En Python, / devuelve un float incluso
cuando el resultado es exacto. // redondea hacia abajo, tambien con negativos.
El resto % cumple a = (a // b) * b + (a % b) para b distinto de cero.
"""

a = 12
b = 5

print(f"a = {a}, b = {b}")
print("Suma (+):", a + b)
print("Resta (-):", a - b)
print("Multiplicacion (*):", a * b)
print("Division (/):", a / b)
print("Division entera (//):", a // b)
print("Resto (%):", a % b)
print("Potencia (**):", a ** b)

# La division por cero produce ZeroDivisionError, por eso no se ejecuta aqui.
print("\nDivision negativa hacia abajo:", -7 // 3)

# Los parentesis ayudan a dejar clara la precedencia de las operaciones.
promedio = (8 + 10) / 2
print("Promedio de 8 y 10:", promedio)
print("Sin parentesis, multiplicacion va antes que suma:", 2 + 3 * 4)

# Las asignaciones aumentadas actualizan la variable.
contador = 4
contador += 3
contador *= 2
print("\nContador despues de += 3 y *= 2:", contador)
