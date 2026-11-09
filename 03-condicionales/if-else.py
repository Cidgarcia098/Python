# if True:
#    print("Esto se ejecuta porque la condición es verdadera")
# else: false:
#    print("Esto se ejecuta porque la condición es falsa")
    
# la_edad = 20
# if la_edad >= 18:
#    print("Eres mayor de edad.")
#else:
#    print("No eres mayor de edad.")
    
"""Uso de if-else:

`if` evalúa una condición y ejecuta un bloque cuando es verdadera; `else`
ejecuta la alternativa cuando es falsa. Sirve para elegir entre dos acciones,
como iniciar sesión solo si la contraseña coincide o mostrar si una persona
es mayor de edad según su edad.

Si hay más de dos alternativas, se puede añadir `elif`. Estos ejemplos son
didácticos: guardar una contraseña directamente en el código no es seguro
para una aplicación real.
"""

contraseña_almacenada = "ricardoMaestro"
contraseña_escrita = "ricardo"
print(contraseña_almacenada == contraseña_escrita) 
# nos devuelve False, ya que no son iguales

contraseña_ingresada = input("Ingrese su contraseña: ")

if contraseña_almacenada == contraseña_ingresada:
    print("iniciar sesion...")
else:
    print("Contraseña incorrecta.")
    
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
