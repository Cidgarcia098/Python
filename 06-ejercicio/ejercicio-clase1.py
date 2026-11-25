#
# promedio de duracion
lista = list(["ricardo", "patricio", '4'])
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 5
logrado= 1.5

#clausulas de matematicas: primero la division, 
# segundo la multiplicacion, luego la resta
#diferencias de duracion
diferencia_con_min = 100 - logrado / otros_cursos_min * 100
diferencia_con_max = 100 - logrado / otros_cursos_promedio * 100
diferencia_con_promedio = 100 - logrado * 1000 // otros_cursos_max / 10
diferencia_con_promedio_round = round(100 - (logrado/otros_cursos_max)*100, 2) 
#el round es para epecificar la cantidad de numeros decimales 
# al final se le añade un 2 para que nos de 2 decimales y no 
# un numero cientifico largo 

#print(f'logrado en {diferencia_con_promedio}% menos que el mas rapido')
#print(f'{diferencia_con_min}% menos que la minima')
#print(f'{diferencia_con_promedio_round}% menos que la maxima')

crudo_promedio = 5
crudo_ricky = 3.5
su = (60+60+60+60+60) * 5
print(su) 

crudo = round(crudo_promedio / crudo_ricky *100, 2)
print(f'{crudo}% ganancia de tiempo = a otros')
