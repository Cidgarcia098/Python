
#lista = (1,2,3,5,4,9)
def suma(nombre, *numeros):
    return f"({nombre},la suma de numeros es: {sum(numeros)})"
resultado = suma("master",0,1,2,3,4,5,6)
print(resultado)