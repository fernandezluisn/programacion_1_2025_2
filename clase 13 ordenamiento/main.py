from ordenamiento import *

lista = [9, 3, 2, 7, 5, 4, 1, 3, 9, 11]
#[1, 3, 2, 7, 5, 4, 9]
#[1, 2, 3, 7, 5, 4, 9]
#[1, 2, 3, 7, 5, 4, 9]
#[1, 2, 3, 4, 5, 7, 9]
#[1, 2, 3, 4, 5, 7, 9]

lista_ordenada = ordenar_x_insercion(lista)

print(lista_ordenada)