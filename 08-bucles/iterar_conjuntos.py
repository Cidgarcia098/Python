"""
ITERACIÓN DE CONJUNTOS (SET) EN PYTHON

Los conjuntos (sets) en Python son colecciones desordenadas de elementos únicos.
A diferencia de las listas o tuplas, los conjuntos no tienen un orden definido,
por lo que no puedes acceder a sus elementos mediante índices (ej. conjunto[0] no funciona).

Sin embargo, al igual que otras colecciones, son iterables, lo que significa que
podemos recorrer sus elementos utilizando un bucle 'for'.

Puntos clave:
1. No tienen orden: El orden en que se imprimen puede variar.
2. Elementos únicos: No permiten duplicados.
3. Iteración: Se realiza igual que en listas o tuplas, pero sin garantía de orden.
"""

# Ejemplo 1: Iteración básica de un conjunto
conjunto_frutas = {"manzana", "pera", "naranja", "uva"}

print("--- Iterando conjunto de frutas ---")
for fruta in conjunto_frutas:
    print(f"Fruta: {fruta}")

# Ejemplo 2: Iteración con números
conjunto_numeros = {1, 2, 3, 4, 5}

print("\n--- Iterando conjunto de números ---")
for numero in conjunto_numeros:
    print(f"Número: {numero}")

# Ejemplo 3: ¿Qué pasa si intentamos usar un índice?
# Esto daría un error: TypeError: 'set' object is not subscriptable
# print(conjunto_frutas[0]) 

# Nota: Si necesitas un orden específico o acceso por índice, 
# deberías convertir el conjunto a una lista:
# lista_frutas = list(conjunto_frutas)
# print(lista_frutas[0])
