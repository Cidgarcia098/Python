numeros = [4,7,1,12,9]

# mayor 
print(max(numeros))
# menor
print(min(numeros))

numero = 122.0021# redondeo
print(f" redondeo {round(numero, 3)}, round") # 3 decimales

#funcion bool
print(bool(0)) # False 
print(bool(1)) # True
# bool (bool([)) # False
# bool([]) # False
# bool detecta caracteres diferentes de cero o vacíos

# funcion all
print(all([True, True, True])) # True
# funcion all con un False
print(all([True, False, True])) # False
# funcion sum
print(sum(numeros)) # 33

#all detecta vacios y responde false 
# "a" "" "c" , 
# # si hay un vacio print(all(["a", "", "c"])) # False

