# Lista de animales (colección ordenada de elementos)
animales = ["pez", "gato", "burro", "cocodrillo"]

# Iteramos sobre la lista: en cada vuelta, 'animal' toma el valor del elemento actual
for animal in animales:
    print(f"bucle_animal: {animal}")

# Tupla de números (colección inmutable)
numeros = (10, 20, 30, 40, 50)

# Iteramos sobre la tupla: multiplicamos cada número por 10 y mostramos el resultado
for numero in numeros:
    resultado = numero * 10
    print(resultado)

"""
EXPLICACIÓN TÉCNICA DEL BUCLE FOR:

1. La estructura 'for': Es un bucle de iteración definida. Se utiliza para recorrer colecciones
   (listas, tuplas, diccionarios, rangos, etc.) elemento por elemento.

2. La variable de iteración ('animal' o 'numero'): Es una variable temporal que actúa como un
   'contenedor' o 'puntero'. En cada iteración, Python asigna automáticamente el valor del
   siguiente elemento de la colección a esta variable. No es necesario declararla previamente.

3. El operador 'in': Es el encargado de establecer la relación de pertenencia. Indica que la
   variable de iteración debe extraer valores desde el objeto iterable que le sigue.

4. Iterables: Son los objetos que pueden ser recorridos (como 'animales' o 'numeros').

5. Función 'zip()' (Concepto adicional): Se utiliza para iterar sobre dos o más colecciones
   simultáneamente. Ejemplo:
   for animal, numero in zip(animales, numeros):
       print(f"{animal} tiene el número {numero}")
   Esto empareja los elementos por índice (el primero con el primero, el segundo con el segundo).
"""

# Un diccionario tiene clave (key) y valor (value)
usuario = {
    "nombre": "Ricky",
    "apellido": "Cid",
    "edad": 25
}

print(type(usuario))
# Usamos .items() para obtener ambos al mismo tiempo
for clave, valor in usuario.items():
    print(f"La clave es: {clave} y el valor es: {valor}")

for  animal, numero in zip(animales, numeros):
    resultados=animal * numero
    
    print(f"El animal es {animal} y el número es {numero}")
    print(resultados)
    print(f"animal es multiplicado por {numero} es: {resultado}")
    print(animal)
    print(numero)
    
    
    # range
    for i in range(5):
        resultadoi= i+1
        print(resultadoi) # imprime: 1, 2, 3, 4, 5)  # imprime:0, 1,2,3, 4,

for usuario in enumerate(usuario.items()):
    indice = usuario[0]+1
    clave = usuario[1][0]
    valor = usuario [1][1]
    
    print(f"Índice: {indice}, Clave: {clave}, Valor: {valor}")

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"id: {indice}, animales {valor}")
else:
    print("el bucle termino")
    
# es el mismo metodo para iterar conjuntos y tuplas