"""Clase: conjuntos (set) y frozenset en Python."""

# Un conjunto guarda elementos unicos: si agregamos un valor repetido,
# Python lo conserva una sola vez. No tiene posiciones ni orden garantizado.
# Por eso se consulta con "in", pero no se accede con indices como conjunto[0].

# 1. Crear un conjunto con llaves.
frutas = {"manzana", "banana", "pera"}
print("Conjunto de frutas:", frutas)

# Para crear un conjunto vacio hay que usar set().
# {} crea un diccionario vacio, no un conjunto.
conjunto_vacio = set()
diccionario_vacio = {}
print("Conjunto vacio:", conjunto_vacio)
print("Tipo de {}:", type(diccionario_vacio))

# 2. Crear conjuntos desde otros iterables con set().
# Los valores repetidos desaparecen al convertir la lista.
numeros_repetidos = [1, 2, 2, 3, 3, 3]
numeros_unicos = set(numeros_repetidos)
print("Lista original:", numeros_repetidos)
print("Convertida a conjunto:", numeros_unicos)

# Tambien se puede convertir un texto: cada caracter pasa a ser un elemento.
# El orden al imprimir un conjunto puede variar.
letras = set("banana")
print("Letras unicas de banana:", letras)

# 3. Consultar si un elemento pertenece al conjunto.
print("Hay banana?", "banana" in frutas)
print("Hay naranja?", "naranja" in frutas)

# 4. Agregar o quitar elementos. Estos metodos modifican el conjunto original.
colores = {"rojo", "azul"}
colores.add("verde")  # add() agrega un elemento.
colores.update(["amarillo", "rojo"])  # update() agrega varios; ignora repetidos.
print("Despues de agregar:", colores)

colores.discard("negro")  # discard() no da error si el elemento no existe.
colores.remove("amarillo")  # remove() elimina un elemento que si existe.
print("Despues de quitar elementos:", colores)

# 5. Operaciones entre conjuntos.
# Los conjuntos de ejemplo comparten "banana" y "pera".
frutas_tropicales = {"banana", "pera", "mango"}
print("Union (todos):", frutas | frutas_tropicales)
print("Interseccion (en ambos):", frutas & frutas_tropicales)
print("Diferencia (solo en frutas):", frutas - frutas_tropicales)
print("Diferencia simetrica (no en ambos):", frutas ^ frutas_tropicales)

# 6. Comparacion con otras colecciones.
# Lista: conserva orden y permite repetidos; se puede modificar.
lista_ejemplo = ["rojo", "azul", "rojo"]

# Tupla: conserva orden y permite repetidos; no se puede modificar.
tupla_ejemplo = ("rojo", "azul", "rojo")

# Conjunto: no conserva un orden garantizado, no repite valores y se modifica.
conjunto_ejemplo = {"rojo", "azul", "rojo"}
print("Lista:", lista_ejemplo)
print("Tupla:", tupla_ejemplo)
print("Conjunto (sin repetidos):", conjunto_ejemplo)

# Los elementos de un set deben ser hashables. Una lista no cumple ese
# requisito, pero frozenset si puede incluirse porque es inmutable.
coordenadas = frozenset([10, 20])
conjunto_de_conjuntos = {coordenadas, frozenset([30, 40])}
print("Conjunto de frozenset:", conjunto_de_conjuntos)

# frozenset se parece a set, pero no permite agregar ni quitar elementos.
print("frozenset de coordenadas:", coordenadas)

# 7. Subconjuntos y superconjuntos.
# A es subconjunto de B si todos los elementos de A tambien estan en B.
conjunto_base = {1, 2, 3, 4}
posible_subconjunto = {1, 2, 3}
no_es_subconjunto = {2, 5}

print("\nSubconjuntos:")
print(
    "posible_subconjunto.issubset(conjunto_base):",
    posible_subconjunto.issubset(conjunto_base),
)
print(
    "no_es_subconjunto.issubset(conjunto_base):",
    no_es_subconjunto.issubset(conjunto_base),
)

# <= comprueba lo mismo que issubset(), e incluye el caso en que ambos
# conjuntos sean iguales. < comprueba un subconjunto propio: no son iguales.
print("Con <=:", posible_subconjunto <= conjunto_base)
print("Subconjunto propio con <:", posible_subconjunto < conjunto_base)
print("Un conjunto no es subconjunto propio de si mismo:", conjunto_base < conjunto_base)

# B es superconjunto de A si contiene todos los elementos de A.
# issuperset() y >= comprueban esa relacion desde el otro conjunto.
print(
    "conjunto_base.issuperset(posible_subconjunto):",
    conjunto_base.issuperset(posible_subconjunto),
)
print("Con >=:", conjunto_base >= posible_subconjunto)

# 8. Conjuntos disjuntos: no tienen ningun elemento en comun.
# isdisjoint(otro) devuelve True si no comparten elementos y False si comparten
# al menos uno. En este primer ejemplo comparten 1, 2 y 3.
print(
    "conjunto_base y posible_subconjunto son disjuntos?:",
    conjunto_base.isdisjoint(posible_subconjunto),
)

# Este conjunto no comparte elementos con conjunto_base, por eso devuelve True.
conjunto_sin_elementos_en_comun = {5, 6}
print(
    "conjunto_base y conjunto_sin_elementos_en_comun son disjuntos?:",
    conjunto_base.isdisjoint(conjunto_sin_elementos_en_comun),
)
# 9. Operaciones matemáticas simples y limpieza de errores.
division = 2 / 2
print(f"\nLa división de 2 / 2 es: {division}")

suma = 2 + 2
print(f"La suma de 2 + 2 es: {suma}")

resta = 2 - 2
print(f"La resta de 2 - 2 es: {resta}")
multiplicacion = 2 * 2
print(f"La multiplicación de 2 * 2 es: {multiplicacion}")
division_entera = 2 // 2
print( )


hola_mundo = "hola mundo"
print(f"Mensaje final: {hola_mundo}")
print(hola_mundo)
