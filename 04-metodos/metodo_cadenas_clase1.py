"""Clase 1: primeros metodos de las cadenas (str)

Un metodo es una accion asociada a un valor. Se llama con un punto, parentesis
y, cuando hace falta, argumentos:

    valor.metodo(argumentos)

Los metodos de str ayudan a transformar y consultar texto. Las cadenas son
inmutables: un metodo como upper() no cambia la cadena original, sino que
devuelve una nueva. Hay que guardar ese resultado si queremos reutilizarlo.
"""

saludo = "  Hola, mundo!  "

print("Texto original:", repr(saludo))
print("En mayusculas:", saludo.upper())
print("En minusculas:", saludo.lower())
print("Sin espacios de los extremos:", saludo.strip())

# La variable original conserva sus espacios y mayusculas.
print("Original despues de llamar los metodos:", repr(saludo))

# Se pueden encadenar metodos: primero se quitan espacios y luego se cambia
# el texto a mayusculas. Cada metodo recibe el resultado del anterior.
saludo_limpio = saludo.strip().upper()
print("Resultado encadenado:", saludo_limpio)

# len() es una funcion incorporada, no un metodo de las cadenas.
print("Cantidad de caracteres:", len(saludo_limpio))

# dir() permite explorar nombres disponibles para un objeto. Para ver
# solamente algunos metodos de texto, filtramos la lista que devuelve.
metodos_de_texto = [
    nombre for nombre in dir(saludo)
    if not nombre.startswith("_")
]
print("Algunos nombres disponibles en str:", metodos_de_texto[:4])
