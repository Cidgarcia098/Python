
######### Variables declaradas mediante input #################
nombre1 = input("Ingrese su nombre: ")
print("Hola, " + nombre1 + " --- Primer problema resuelto.")
###############################################################

############## Variables declaradas ###########################
nombre2 = "atentamente_juan"
print(nombre2 + " --- Segundo problema resuelto.")
###############################################################

######$"""""" Variables declaradas y asignadas """"""##########
nombre3 = "atentamente_juan " + "--- Tercer problema resuelto."
print(nombre3)
###############################################################

###"" Variables con números (solo imprime la última modificación)###

# el numero se reemplaza porque luego se modifica.
numero3 = 10
# Se actualiza el valor y luego se incrementa.
numero3 = 10 + 1
numero3 += 5 
print(str(numero3) + " --- Tercer problema resuelto.") #16
# ! Se debe convertir a str para poder concatenar.
##################################################################

###"""""""""""""""""""" Variables con palabras ###################

nombre4 = "Juan"  # Se reemplaza en las siguientes asignaciones.
nombre4 = "Marcos" # se actualiza el valor de la variable.
nombre4 = "Lucas"  # se actualiza el valor de la variable.
nombre4 = "Pérez" # se imprime este ultimo actualizado.
print(nombre4 + " --- Cuarto problema resuelto.")
#################################################################

#"""""""" Concatenación de variables ############################

nombre5 = "lucas"
bienvenido = "Hola, " + nombre5 + " --- Quinto problema resuelto."
print(bienvenido)
#################################################################

#"#########"""""""""""""""variantes con f-strings ###############

nombre6 = "Lucas"
bienvenido2 = f"Hola, {nombre6} --- Sexto problema resuelto." 
print(bienvenido2)
# se usa la f y {...} , esto reemplaza "+" 
# y permite concatenar variables dentro de un string.
# convierte a str automáticamente, no es necesario usar str() para concatenar.
# str( es para convertir en texto) + " texto"  

# otra practica
# si ponemos "del nombre6" borra el valor de la variable
# y no se imprime. "del" es para eliminar la variable.
"""del nombre6"""
###############################################################################

#""operadores de pertenencia (in y not in) en Python""######################
"""flase y true"""""""""""
nombre7 = "Ricardo"
bienvenido7 = f"Hola, {nombre7} --- Séptimo problema resuelto."
# responde True porque Ricardo está en la variable bienvenido7
print("Ricardo" in bienvenido7)
# responde false porque Ricardo está en la variable bienvenido7
print("Juan" in bienvenido7)
# responde False porque Juan no está en la variable
print ("Ricardo" not in bienvenido7) #false
print("problema septimo resuelto.") 

