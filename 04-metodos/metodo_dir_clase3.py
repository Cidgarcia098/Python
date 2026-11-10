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

    # nombre.startswith("_")
    # comprueba si el texto guardado
    # en nombre comienza con _ (guion bajo)
    # if not ... significa “si no...”. Así que 
    # solo conserva los nombres que no empiezan con _. 
    # Esto suele quitar métodos especiales de Python, como __class__
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

# get(clave) busca el valor asociado a esa clave. Si la clave no existe,
# get() devuelve el valor alternativo indicado en el segundo argumento, en
# vez de producir un error.
print("\nEjemplo de get():")
print("Nombre:", persona.get("nombre"))
print("Ciudad:", persona.get("ciudad", "No especificada"))

# keys() devuelve las claves del diccionario; values() devuelve los valores
# en el mismo orden. list() convierte esos resultados en listas para verlos
# claramente al imprimirlos.
print("\nEjemplo de keys() y values():")
print("Claves:", list(persona.keys()))
print("Valores:", list(persona.values()))

# items() permite recorrer cada entrada como un par (clave, valor). En cada
# vuelta, el for guarda las dos partes en sus variables y las muestra.
print("\nEjemplo de items():")
for clave, valor in persona.items():
    print(f"- {clave}: {valor}")

# update() agrega una nueva clave o reemplaza su valor si ya existia.
print("\nEjemplo de update():")
persona.update({"ciudad": "Buenos Aires"})
print("Se agrego la ciudad:", persona["ciudad"])

# pop() elimina la clave indicada y devuelve el valor que tenia guardado.
# Aqui se guarda ese valor para poder mostrarlo despues de eliminarlo.
print("\nEjemplo de pop():")
edad_eliminada = persona.pop("edad")
print("Valor devuelto por pop() (edad):", edad_eliminada)
print("Diccionario despues de pop():", persona)

# clear() elimina todos los elementos. Se aplica a una copia para vaciarla
# sin perder los datos de persona.
print("\nEjemplo de clear():")
copia = persona.copy()
copia.clear()
print("Copia despues de clear() (queda vacia):", copia)

###terminal###################################################
# Algunos nombres disponibles en un diccionario:
#['clear', 'copy', 'fromkeys', 'get', 'items', 
# 'keys', 'pop', 'popitem', 
# 'setdefault', 'update', 'values']

#Metodos habituales de dict:
#get(): obtiene un valor sin error si la clave falta.
#keys(): permite consultar las claves.
#values(): permite consultar los valores.
#items(): permite recorrer pares de clave y valor.
#update(): agrega o actualiza elementos.
#pop(): elimina una clave y devuelve su valor.

#Ejemplo de get():
#Nombre: Juan
#Ciudad: No especificada

#Ejemplo de keys() y values():
#Claves: ['nombre', 'apellido', 'edad']
#Valores: ['Juan', 'Perez', 25]

#Ejemplo de items():
#- nombre: Juan
#- apellido: Perez
#- edad: 25

#Ejemplo de update():
#Se agrego la ciudad: Buenos Aires

#Ejemplo de pop():
#Valor devuelto por pop() (edad): 25
#Diccionario despues de pop(): {'nombre': 'Juan', 'apellido': 'Perez', 'ciudad': 'Buenos Aires'}

#Ejemplo de clear():
#Copia despues de clear() (queda vacia): {}