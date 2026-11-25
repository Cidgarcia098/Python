"""Clase 2: buscar, comprobar y dividir cadenas

Estos ejemplos continuan la leccion de str. Muchos metodos de cadenas
devuelven un resultado nuevo; no modifican el texto original.

Busqueda:
- find(texto) devuelve la posicion de la primera coincidencia o -1.
- index(texto) tambien busca, pero genera ValueError si no encuentra el texto.
- count(texto) cuenta las coincidencias que no se superponen.

Comprobaciones como isalpha() devuelven True o False. Algunos metodos, como
isalpha(), consideran que los espacios no son letras.
"""

frase = "Hola, soy Ricky"
print("Frase:", frase)
print("Posicion de 'soy':", frase.find("soy"))
print("Posicion de 'Python' (no aparece):", frase.find("Python"))
print("Cantidad de letras 'o':", frase.count("o"))
print("Empieza con 'Hola':", frase.startswith("Hola"))
print("Termina con 'Ricky':", frase.endswith("Ricky"))

palabra = "Python"
numero_como_texto = "2026"
texto_con_espacio = "Hola mundo"
print("\nSolo letras:", palabra.isalpha())
print("Solo digitos:", numero_como_texto.isdigit())
print("Letras y espacios:", texto_con_espacio.isalpha())
print("Letras y espacios son alfanumericos:", texto_con_espacio.isalnum())

# strip() elimina caracteres de los extremos, no del medio.
entrada = "   Ana Perez   "
nombre = entrada.strip()
print("\nEntrada:", repr(entrada))
print("Despues de strip():", repr(nombre))

# split() divide una cadena y devuelve una lista.
palabras = nombre.split()
print("Lista de palabras:", palabras)

# join() une elementos de texto usando la cadena que lo llama como separador.
nombre_con_guion = "-".join(palabras)
print("Unido con guiones:", nombre_con_guion)

# replace() devuelve una nueva cadena con las coincidencias reemplazadas.
frase_nueva = frase.replace("Ricky", "Ricardo")
print("\nFrase original:", frase)
print("Frase con replace():", frase_nueva)

# capitalize() pone en mayuscula la primera letra y en minuscula el resto.
print("capitalize():", "hOLA MUNDO".capitalize())
print("title():", "hola mundo".title())
