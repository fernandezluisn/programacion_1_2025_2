from paquete import *

lista_a = [3, 7, 9]
lista_b = [5, 7, 9]

print(calcular_interseccion(lista_a, lista_b))

lista_1 = [1, 2, 4]
lista_2 = [1, 3, 4]

union = [1, 2, 3, 4]

print(calcular_union(lista_1, lista_2))
print(calcular_union_optimizado(lista_1, lista_2))

print("Diferencia: ")
print(calcular_diferencia(lista_1, lista_2))
print(calcular_diferencia(lista_2, lista_1))

