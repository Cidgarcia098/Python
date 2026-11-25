frase =input('decime unas palablas o frase y yo te digo cuanto tardarias: ')

cantidad_de_palabras = frase.split(" ")
cuenta_las_palabras = len(cantidad_de_palabras)

# Calculamos el tiempo que tardaría una persona promedio en decir la frase
# (asumiendo 2 palabras por segundo)
tiempo_tardado = cuenta_las_palabras / 2

print(f'Dijiste {cuenta_las_palabras} palabras, y tardarías {tiempo_tardado} segundos en decirlas.')
if cuenta_las_palabras >= 50:
    print("¡Wow! Dijiste demasiadas palabras, ¡para un poco!")
elif cuenta_las_palabras <= 3:
    print(f"'{frase}'... eso fue muy corto, intenta decir algo más largo.")
else:
    print(f"Está bien, puedes seguir escribiendo.")

