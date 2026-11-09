# Tipos de variables en Python

# camelcase
NombreCompleto = "Ricardo Patricio"

# snake_case
apellido_completo = "Cid Garcia"

# concatenation con +
bienvenido = "NombreCompleto" + "apellido_completo"

# concatenacion con f-string
bienvenido = f"hola {NombreCompleto} ¿como estas?"
bienvenido = f"hola {apellido_completo} ¿como estas?"

# operadores de pertenencia (in / not in)
print("Ricardo" in NombreCompleto)  # True
print("Ricardo" in apellido_completo)  # False

print("Ricardo" not in apellido_completo)  # False

##"""""""""""""""""""""""""""""""""""""""""""""""""""""""
# crear listas ##########################################

Lista = ["Ricardo", "Patricio", "Cid", "Garcia"]
print(Lista[0] + " lista")  
# se puede imprimir por indice

# crear tuplas ###########################################
#upla = ("Ricardo", "Patricio", "Cid", "Garcia")
#rint(Tupla[0] + " tupla")  # se puede imprimir por indice

# crear conjuntos #########################################  
conjunto = {"Ricardo", "Patricio", "Cid", "Garcia"}
print(conjunto) 
# no se puede imprimir por indice, ya que no tiene orden

# creando un diccionario (dict)
diccionario = {
    "nombre": "Ricardo",
    "segundo_nombre": "Patricio",
    "apellido": "Ciddd",
    "segundo_apellido": "Garcia",
    "gusto_por_programar" : True
} 
print(diccionario)
print(diccionario["apellido"]) # se puede imprimir por clave
#key: valor
# 1 "nombre" es la clave y "Ricardo" es el valor
# 2 las claves tambien 
# tienen un numero de indentificacion "nombre" seria 0
# las comas siempre se ponen al final de cada clave:valor, menos en la ultima
# formas de imprimir un diccionario:
print(diccionario["nombre"])  # se puede imprimir por clave
print(diccionario.get("apellido"))  # se puede imprimir por clave

###########################################################
conjunto = {"Ricardo", "Patricio", "Cid", "Garcia", "ricardo", "ricardo", "ricardo"}
tupla = ("Ricardo", "Patricio", "Cid", "Garcia")
# la diferencia entre un conjunto y una tupla
# es que el conjunto no tiene orden, 
# mientras que la tupla si lo tiene
# ademas la tupla imprime todo y 
# conjunto no imprime palabras repetidas
print(tupla[0], tupla[1], tupla[2], tupla[3])
print("conjunto: ", conjunto)
