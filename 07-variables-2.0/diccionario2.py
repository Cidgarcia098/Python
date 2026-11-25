# diccionario desde dict()
# diccionario desde {}

diccionario_vacio = dict()
diccionario_vacio = {}

# diccionario con elementos
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# acceder a elementos
print(diccionario["nombre"])

# modificar elementos
diccionario["edad"] = 26

# agregar elementos
diccionario["profesion"] = "Ingeniero"

# eliminar elementos
del diccionario["ciudad"]

# verificar si una clave existe
if "nombre" in diccionario:
    print("La clave 'nombre' existe en el diccionario")

# iterar sobre el diccionario 
for clave, valor in diccionario.items():
    print(f"interar {clave}: {valor} ")

# limpiar el diccionario (esto está fuera del for, a la misma altura)
diccionario.clear()
print("Diccionario limpiado")

# --- TEMAS AVANZADOS ---

# 1. Uso de .get() para evitar errores (KeyError)
usuario = {"nombre": "Maria", "edad": 30}
edad = usuario.get("edad", "No disponible")
pais = usuario.get("pais", "Desconocido") # Devuelve valor por defecto
print("Edad:", edad, "País:", pais)
print(f"ProblemaUno: {usuario}")
# 2. Diccionarios anidados
empleados = {
    "id_001": {"nombre": "Ana", "puesto": "Gerente"},
    "id_002": {"nombre": "Luis", "puesto": "Desarrollador"}
}
print(f"EmpleadosProblema2 {empleados["id_001"]}")
# 3. dict.fromkeys() - Crea un diccionario con claves dadas y valor inicial común
claves = ("nombre", "edad", "puesto")
nuevo_diccionario = dict.fromkeys(claves, "Desconocido")
print(f"3Diccionario desde claves: {nuevo_diccionario}")

for clave in claves:
    print(f"{clave} por#3: {claves}")

clave2 = ("nombre", "edad", "puesto")
clave2puntos= dict.fromkeys(clave2, "datos")
print(f"clave2puntos {clave2puntos}")

# 4. Diccionario por comprensión 
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados **2 rango del 1-6: {cuadrados}")

# 5. Unir diccionarios (Python 3.9+)
datos1 = {"a": 1, "b": 2}
datos2 = {"c": 3, "d": 4}
fusionados = datos1 | datos2
print(f"Diccionarios unidos: {fusionados}")

# Nota: frozenset no es un método de diccionario, es un tipo de dato
# (un conjunto inmutable) que puede usarse como clave en un diccionario,
# a diferencia de las listas o diccionarios que son mutables.
f_set = frozenset(["a", "b", "c"])
diccionario_con_frozenset = {f_set: "valor asociado"}
print(f"Diccionario con frozenset: {diccionario_con_frozenset}")

f_frozemset = (frozenset([1, 2, 3]), "jajaja") # Error: frozenset solo acepta un iterable
fronze = {f_frozemset : "valor"}

print(f"Frozenset creado: {fronze}")

diccionario = {frozenset(["nombre", "apellido"]) : "jajaja"}
diccionario = dict.fromkeys({"ABCDE"}) #"none"
print = print(diccionario)

#print(f"Diccionario con frozenset creado directamente: {dic}")

#dic_fromkey = dict.fromkeys(["nombre", "edad"], "valor_por_defecto")
#dic_fromkey = dict.fromkeys({"nombre", "edad"}, "fromkeys")
#print(f"Diccionario con fromkeys: {dic_fromkey}")
