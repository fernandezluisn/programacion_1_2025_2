from paquete.funciones import *

matriz_notas = [[5, 6, 7, 4],
                [8, 9, 5, 4],
                [5, 4, 4, 4],
                [4, 2, 6, 4]]

alumnos = ["Pedro", "Juan", "Brian", "José"]
materias = ["Progra 1", "Matemática", "Arquitectura y sistemas operativos", "Inglés"]

# for i in range(len(matriz_notas)):
#     for j in range(len(matriz_notas[i])):

#         print(f"El alumno {alumnos[i]} en {materias[j]} tuvo de nota {matriz_notas[i][j]}")

ejecutar = True

while ejecutar:

    print("Seleccione tarea que desea realizar: ")
    print("1- buscar notas por alumno")
    print("2- buscar alumno con mejor promedio")
    print("3- buscar notas por materia")
    print("4- recorrer diagonal")
    print("9- finalizar")

    tarea = int(input("Ingrese número de tarea: "))

    match tarea:
        case 1:
            nombre = input("Ingrese el nombre del alumno: ")
            fila = buscar_texto(nombre, alumnos)

            if fila != None:
                print(f"Las notas de {nombre} son:")
                for i in range(len(matriz_notas)):
                    print(f"{materias[i]} = {matriz_notas[fila][i]}")
            else:
                print("El alumno no fue encontrado")

            print("")
        
        case 3:
            materia = input("Ingrese el nombre de la materia: ")
            columna = buscar_texto(materia, materias)

            if columna != None:
                print(f"Las notas de {materia} son:")
                for i in range(len(matriz_notas)):
                    print(f"{alumnos[i]} = {matriz_notas[i][columna]}")
            else:
                print("La materia no fue encontrada")
            
            print("")
        
        case 4:
            #Una vez que validamos que la mátriz es cuadrada
            for i in range(len(matriz_notas)):
                print(f"{matriz_notas[i][i]}")
        case 9:
            ejecutar = False
        
        case _: 
            print("Opción no válida")
            
