"""Clase 2: tipos de datos compuestos

Los tipos compuestos permiten agrupar varios valores:
- list: coleccion ordenada y modificable; se escribe con corchetes.
- tuple: coleccion ordenada que no se modifica; se escribe con parentesis.
- set: conjunto sin posiciones; no conserva elementos duplicados.
- dict: relaciona claves con valores; se consulta usando una clave.

Los indices de las secuencias (list y tuple) empiezan en cero. Los conjuntos
no se consultan por indice. Las claves de un diccionario no son posiciones.
"""

colores = ["rojo", "verde", "azul"]
coordenada = (10, 20)
etiquetas = {"python", "curso", "python"}
persona = {
    "nombre": "Lucia",
    "edad": 20,
}

print("Lista completa:", colores)
print("Primer color, indice 0:", colores[0])

# Las listas son modificables.
colores.append("amarillo")
print("Lista despues de append():", colores)

print("\nTupla:", coordenada)
print("Primer valor de la tupla:", coordenada[0])

# El conjunto elimina el valor repetido y no tiene un orden para indexar.
print("\nConjunto sin duplicados:", etiquetas)
print("'curso' esta en el conjunto:", "curso" in etiquetas)

print("\nDiccionario:", persona)
print("Nombre por clave:", persona["nombre"])
print("Ciudad con valor alternativo:", persona.get("ciudad", "Sin indicar"))

# Se puede recorrer un diccionario como pares clave-valor.
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

print("\nTipos:")
for valor in (colores, coordenada, etiquetas, persona):
    print(type(valor).__name__)
