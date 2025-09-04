#Suponemos que queremos calcular el promedio de las notas de un alumno
notas_alumno = [2, 7, 8, 9, 10, 5, 3, 1]
suma = 0

for i in range(len(notas_alumno)):

    print(f"El indice es {i}")
    print(f"La nota es {notas_alumno[i]}")
    print()
    suma += notas_alumno[i]

promedio = suma / len(notas_alumno)

print(f"El promedio es: {promedio}")


