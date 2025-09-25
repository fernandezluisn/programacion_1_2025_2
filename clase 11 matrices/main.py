from paquete.matrices import *

alumno_1 = [4, 7, 8]
alumno_2 = [7, 9, 5]
alumno_3 = [4, 2, 7]

matriz_notas = [alumno_1, 
                alumno_2,
                alumno_3]

#print(matriz_notas)

alumno_1 = ["Perez", "José", 18]
alumno_2 = ["Suarez", "Nicolas", 20]
alumno_3 = ["Díaz", "Juan", 19]
alumno_4 = ["Ramírez", "Pedro", 30]
alumna_5 = ["Barceló", "Daniela", 24]

matriz_alumnos = [alumno_1,
                  alumno_2,
                  alumno_3,
                  alumno_4,
                  alumna_5]

print(matriz_alumnos[2][1])


print(matriz_alumnos)

matriz_alumnos[1][1] = "Francisco"


lista_3 = [[1, 2, 3], 
           [4, 5, 6]]

mostrar_matriz(matriz_alumnos)

matriz_inicial = inicializar_matriz(3, 3, "X")

mostrar_matriz(matriz_inicial)

matriz_inicial = cargar_secuencial(matriz_inicial, "Ingrese nota del alumno: ")

mostrar_matriz(matriz_inicial)

matriz_inicial = cargar_distribuido(matriz_inicial, "Ingrese nota correspondiente: ")

mostrar_matriz(matriz_inicial)


    