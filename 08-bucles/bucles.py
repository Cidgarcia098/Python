animales = {"perro": "ladrido", "gato": "maullido", "pajaro": "pio"}
for respuesta in animales:
    print(f"el {respuesta} hace el {animales[respuesta]}")
    

# O también:
for animal, sonido in animales.items():
    print(f"el {animal} hace el {sonido}")

lista = {"manzana": "enero", "pera": "junio", "uva":"septiembre"}
for fruta, MesDeEstacion in lista.items():
    print(f"la {fruta} es de la temporada de: {MesDeEstacion}")
    
# continue: es el elemento que indica que se saltea
# la iteración actual y pasa a la siguiente.
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
for fruta in frutas:
    if fruta=="manzana":
        continue #saltea manzana
    print(f"Fruta: {fruta}")
# break: es el elemento que indica que se detiene
# la ejecución del bucle por completo.
for fruta in frutas:
    if fruta == "pera":
        print("¡Encontré la pera, deteniendo el bucle!")
        break 
    #break finaliza el bucle cuando se encuentra la pera
    print(f"Fruta: {fruta}")
#else para terminar el bucle:
else:
    print("terminado")
