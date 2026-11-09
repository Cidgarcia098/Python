operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
    "multiplicacion": lambda x, y: x * y,
    "division": lambda x, y: x / y
}
suma = operaciones["suma"](5, 3)
resta = operaciones["resta"](5, 3)
multiplicacion = operaciones["multiplicacion"](5, 3)
division = operaciones["division"](5, 3)
multi = (8 * 2)
div = (8 / 2) # la idvision siempre es flotante (float)
potencia = (8 ** 2) # potencia
division_baja = (8 // 2) # division baja, redondea hacia abajo
resto = (8 % 2) # resto de la division
media = (8 + 2) / 2 # media aritmetica
relativa = (8 + 2) / 2 # media relativa
relativa_absulta = (8 + 2) / 2 # media relativa absoluta

print (suma)
print (resta)
print (multiplicacion)
print (division)
print (multi)
print (div)
print (potencia)
print (division_baja)
print (resto)
print (media)
print (relativa)
print (relativa_absulta)

# funcion para obtener el tipo de dato de una variable
# (no son operaciones, pero es importante conocerlos)

tipo_de_dato = type("hola maestro") # tipo de dato no devuelve que tipo de dato es,
tipo_de_dato_numero = type(8) # tipo de dato no devuelve que tipo de dato es,
tipo_de_dato_flotante = type(8.0) # tipo de dato no devuelve que tipo de dato es,
tipo_de_dato_Lista = type([1, 2, 3]) # tipo de dato no devuelve que tipo de dato es,
tipo_de_dato_Tupla = type((1, 2, 3)) #
tipo_de_dato_Conjunto = type({1, 2, 3}) #
tipo_de_dato_Diccionario = type({"nombre": "Juan", "apellido": "Pérez"}) #
tipo_de_dato_Booleano = type(True) #
tipo_de_dato_Nulo = type(None) #
tipo_de_dato_Bytes = type(b"hola") #
tipo_de_dato_Bytearray = type(bytearray(b"hola")) #
tipo_de_dato_Memoria = type(memoryview(b"hola")) #
tipo_de_dato_Rango = type(range(5)) #
tipo_de_dato_Iterador = type(iter([1, 2, 3])) #
tipo_de_dato_Generador = type((x for x in range(5))) #
tipo_de_dato_Excepcion = type(Exception("Error")) #
tipo_de_dato_Funcion = type(lambda x: x) #
tipo_de_dato_Clase = type(type) #
tipo_de_dato_Modulo = type(__import__("math")) #
tipo_de_dato_Objeto = type(object()) #
tipo_de_dato_ClasePersonalizada = type(type("MiClase", (object,), {})) #

print (tipo_de_dato)
print (tipo_de_dato_numero)
print (tipo_de_dato_flotante)
print (tipo_de_dato_Lista) # otras



