bandera = "Si"

acumulador = 0

cantidad_materias = 0

nombre = input("Ingrese el nombre del alumno: ")

while bandera == "Si":

    nota = int(input("Ingrese la nota de la materia: "))

    acumulador += nota
    cantidad_materias += 1

    bandera = input("¿Quiere seguir ingresando notas?: Si/No ")

    
print(f"El promedio del alumno {nombre} es:")
print(f"{acumulador / cantidad_materias}")