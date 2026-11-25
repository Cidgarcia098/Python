"""Clase: distintas formas de crear y usar tuplas en Python."""

# Una tupla guarda varios valores en un orden fijo y permite repetidos.
# A diferencia de una lista, no se puede modificar despues de crearla.

# 1. Crear una tupla escribiendo sus elementos entre parentesis.
tupla_parentesis = ("ricardo", "patricio", "ana")
print("Con parentesis:", tupla_parentesis)

# 2. Los parentesis son opcionales: las comas son las que forman la tupla.
tupla_sin_parentesis = "lunes", "martes", "miercoles"
print("Sin parentesis (empaquetado):", tupla_sin_parentesis)

# 3. Una tupla vacia se puede escribir como () o crear con tuple().
tupla_vacia = ()
tupla_vacia_con_constructor = tuple()
print("Tupla vacia:", tupla_vacia)
print("Otra tupla vacia:", tupla_vacia_con_constructor)

# 4. Para una tupla de un solo elemento, es obligatorio poner una coma.
tupla_de_un_elemento = ("dato",)
no_es_tupla = ("dato")
print("Tupla de un elemento:", tupla_de_un_elemento, type(tupla_de_un_elemento))
print("Sin la coma es texto:", no_es_tupla, type(no_es_tupla))

# 5. tuple(iterable) convierte una secuencia u otro iterable en tupla.
lista_colores = ["rojo", "verde", "azul"]
tupla_desde_lista = tuple(lista_colores)
tupla_desde_texto = tuple("sol")
tupla_desde_rango = tuple(range(1, 4))

print("Desde una lista:", tupla_desde_lista)
print("Desde un texto (un elemento por caracter):", tupla_desde_texto)
print("Desde range(1, 4):", tupla_desde_rango)

# tuple() tambien puede recibir un conjunto, pero el orden del conjunto
# no esta garantizado. Al convertir un diccionario, se obtienen sus claves.
conjunto_numeros = {1, 2, 3}
diccionario = {"nombre": "Ricky", "edad": 20}
print("Desde un conjunto:", tuple(conjunto_numeros))
print("Desde un diccionario (claves):", tuple(diccionario))

# Se accede a los elementos por indice, empezando desde cero.
print("Primer color:", tupla_desde_lista[0])
print("Primeros dos colores:", tupla_desde_lista[:2])

# count() cuenta cuantas veces aparece un valor e index() da su posicion.
tupla_con_repetidos = ("rojo", "azul", "rojo")
print("Veces que aparece rojo:", tupla_con_repetidos.count("rojo"))
print("Posicion de azul:", tupla_con_repetidos.index("azul"))

# Se pueden asignar los elementos a varias variables (desempaquetar).
nombre, apellido = ("Ana", "Perez")
print("Desempaquetado:", nombre, apellido)

# Las tuplas son inmutables: esta asignacion daria TypeError si se ejecuta.
# tupla_parentesis[0] = "cambiado"

# Tipos relacionados, pero distintos:
lista = ["a", "b"]              # Ordenada y modificable.
conjunto = {"a", "b"}           # Valores unicos; no garantiza orden.
diccionario_ejemplo = {"clave": "valor"}  # Guarda pares clave-valor.
print("Lista:", lista)
print("Conjunto:", conjunto)
print("Diccionario:", diccionario_ejemplo)

# namedtuple es una tupla cuyos elementos tambien tienen nombres.
from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])
punto = Punto(3, 5)

print("namedtuple completa:", punto)
print("Acceso por nombre:", punto.x, punto.y)
print("Acceso por indice:", punto[0], punto[1])

punto = namedtuple("punto", ["x", "y"]) 
punto = Punto(10, 20)
print(f"Coordenada X: {punto.x}", 
      f"Coordenada Y: {punto.y}")

