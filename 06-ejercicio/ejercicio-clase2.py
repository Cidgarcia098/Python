# Pedimos al usuario una frase para calcular cuanto tardaria en decirla.
frase = input("Decime una frase y te calculo cuanto tardarias en decirla: ")

# split() separa la frase por espacios (o cualquier espacio en blanco).
# Sin argumentos, tambien ignora espacios repetidos y devuelve [] si no hay texto.
palabras_separadas = frase.split()

# len() cuenta cuantos elementos, en este caso palabras, hay en la lista.
cantidad_de_palabras = len(palabras_separadas)

# Si la frase tiene mas de 120 palabras, mostramos una advertencia.
if cantidad_de_palabras > 120:
    print("Para flaco, tampoco te pedi un testamento.")

# Estimamos que una persona dice 2 palabras por segundo.
segundos_para_decirlo = cantidad_de_palabras / 2
print(
    f"Dijiste {cantidad_de_palabras} palabras, "
    f"y tardarias {segundos_para_decirlo} segundos en decirlo."
)

# Aplicamos el factor 1.3 del ejemplo para calcular el tiempo de Dalto.
segundos_de_dalto = segundos_para_decirlo * 1.3
print(f"Dalto lo diria en {segundos_de_dalto} segundos.")
