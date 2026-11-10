"""Clase 3: explorar los metodos de un diccionario

dir(objeto) es una funcion incorporada que muestra los nombres de atributos
y metodos disponibles para ese objeto. No ejecuta esos metodos.

Los nombres que empiezan con doble guion bajo suelen ser detalles internos;
por eso aqui se filtran para mostrar una lista mas sencilla. La lista puede
variar segun la version de Python.
"""

persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
}

nombres_disponibles = [
    nombre for nombre in dir(persona)
    if not nombre.startswith("_")
]
print("Algunos nombres disponibles en un diccionario:")
print(nombres_disponibles)

print("\nMetodos habituales de dict:")
print("get(): obtiene un valor sin error si la clave falta.")
print("keys(): permite consultar las claves.")
print("values(): permite consultar los valores.")
print("items(): permite recorrer pares de clave y valor.")
print("update(): agrega o actualiza elementos.")
print("pop(): elimina una clave y devuelve su valor.")

# get() permite indicar un valor alternativo si la clave no existe.
print("\nNombre:", persona.get("nombre"))
print("Ciudad:", persona.get("ciudad", "No especificada"))

print("\nClaves:", list(persona.keys()))
print("Valores:", list(persona.values()))
print("Pares:")
for clave, valor in persona.items():
    print(f"- {clave}: {valor}")

# update() modifica el diccionario. pop() elimina la clave indicada.
persona.update({"ciudad": "Buenos Aires"})
edad_eliminada = persona.pop("edad")
print("\nEdad eliminada:", edad_eliminada)
print("Diccionario actualizado:", persona)

# clear() elimina todos los elementos. Lo demostramos sobre una copia para
# conservar el diccionario del ejemplo anterior.
copia = persona.copy()
copia.clear()
print("Copia despues de clear():", copia)
