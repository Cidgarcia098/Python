#def saludar():
    #print("¡Hola!")
#saludar()

#def saludar_nombre(nombre):
    #print(f"¡Hola, {nombre}!")
#saludar_nombre("Ricardo")

#def saludando():
    #print("hola mundo")
#saludando()

#def sumar(a, b):
    #return a + b
#resultado = sumar(5, 3)
#print(resultado)

#def multiplicar(a, b):
    #return a * b
#resultado_multiplicacion = multiplicar(4, 2)
#print(resultado_multiplicacion)

#def dividir(a, b):
#    if b != 0:
#        return a / b
#    else:
#        return "Error: No se puede dividir por cero"
#   resultado_division = dividir(10, 2)
#    print(resultado_division)
#    resultado_division_error = dividir(10, 0)
#    print(resultado_division_error)
#    
#def es_par(numero):
#       if numero % 2 == 0:
#            return True
#        else:
#            return False
#print(es_par(4))
#def saludar_con_defecto(nombre="Usuario"):
#    print(f"Hola, {nombre}!")
    
    

def saludar(nombre, sexo="otro"):
    sexo = sexo.strip().lower()

    if sexo == "femenino":
        adjetivo = "reina"
    elif sexo == "masculino":
        adjetivo = "titán"
    else:
        adjetivo = "crack"

    print(f"Hola {nombre}, mi {adjetivo} ¿Cómo estás?")


def crear_contrasena(num):
    chars = "abcdefgjkopq"

    if not isinstance(num, int) or num < 0:
        raise TypeError("num debe ser un entero mayor o igual que cero")

    primer_numero = int(str(num)[0])
    c1 = (primer_numero - 2) % len(chars)
    c2 = (primer_numero - 3) % len(chars)
    c3 = primer_numero % len(chars)
    contraseña = f"contraseña_aleatoria: {chars[c1]}{chars[c2]}{chars[c3]}{primer_numero * 2}"

    return contraseña, primer_numero


if __name__ == "__main__":
    saludar("Camila", "Femenino")
    saludar("Dalto", "Masculino")
    saludar("Alex", "otro")

    password, primer_numero = crear_contrasena(1)
    print(f"Contraseña: {password}")
    print(f"Primer número: {primer_numero}")

#def crear_contrasena(num):
#    chars = "abcdefgjkopq"
#    simbolo = "@"
#
#    if not isinstance(num, int) or num < 0:
#        raise TypeError("num debe ser un entero mayor o igual que cero")
#
#    digitos = [int(d) for d in str(num)]
#    primer_numero = digitos[0]
#    ultimo_numero = digitos[-1]
#
#    l1 = chars[(primer_numero - 2) % len(chars)]
#    l2 = chars[(primer_numero + ultimo_numero) % len(chars)]
#    l3 = chars[(primer_numero * 3) % len(chars)]
#
#    n1 = primer_numero % 10
#    n2 = (primer_numero * 2) % 10
#    n3 = ultimo_numero % 10
#
#    # Un solo "@" en el medio: letras, "@", y números
#    clave = f"{l1}{l2}{l3}{simbolo}{n1}{n2}{n3}"
#    return f"contraseña_aleatoria: {clave}"
