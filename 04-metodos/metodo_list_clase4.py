"""Clase 4: metodos para trabajar con listas

Las listas son mutables: sus metodos pueden cambiar la lista original.

Metodos para agregar:
- append(elemento) agrega un elemento al final.
- insert(indice, elemento) agrega un elemento en una posicion.
- extend(iterable) agrega varios elementos.

Metodos para quitar:
- remove(valor) elimina la primera coincidencia del valor.
- pop(indice) elimina y devuelve el elemento de esa posicion.
- clear() elimina todos los elementos.

sort() ordena la lista en el mismo lugar y reverse() invierte su orden actual.
Estos metodos modifican la lista y devuelven None; no hay que asignar su
resultado a otra variable.
"""

frutas = ["pera", "manzana"]
print("Lista inicial:", frutas)

frutas.append("naranja")
print("Despues de append():", frutas)

frutas.insert(1, "banana")
print("Despues de insert():", frutas)

frutas.extend(["uva", "kiwi"])
print("Despues de extend():", frutas)

frutas.remove("banana")
print("Despues de remove():", frutas)

fruta_eliminada = frutas.pop(0)
print("Elemento devuelto por pop():", fruta_eliminada)
print("Lista despues de pop():", frutas)

# sorted() crea y devuelve una lista ordenada sin cambiar la original.
frutas_ordenadas = sorted(frutas)
print("\nOrden con sorted():", frutas_ordenadas)
print("Lista original sin cambios:", frutas)

# sort() modifica la lista directamente.
frutas.sort()
print("Lista despues de sort():", frutas)

# reverse() invierte el orden actual; no ordena alfabeticamente.
frutas.reverse()
print("Lista despues de reverse():", frutas)

# len() es una funcion incorporada que cuenta elementos.
print("Cantidad de frutas:", len(frutas))

# clear() borra la lista; se usa una copia para mantener el ejemplo principal.
lista_vacia = frutas.copy()
lista_vacia.clear()
print("Copia despues de clear():", lista_vacia)
