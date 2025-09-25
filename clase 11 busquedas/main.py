from paquete.funciones import *

lista = [3, 5, 6, 8, 9, 11]

#máxima cantidad de iteraciones = tamaño de la lista
pos = buscar_lineal(lista, 8)

print(f"El 8 se encuentra en la posición {pos}")

pos = buscar_lineal(lista, 15)

print(f"El 15 se encuentra en la posición {pos}")

buscar_bin(lista, 3)