tupla = (3, 2, 5)
print(tupla[1])

#tupla[1] = 9

num1, num2, num3 = tupla

print(num1)
print(num2)
print(num3)

def retornar_tupla(lista1: list, lista2: list)-> tuple:

    indice_1 = lista1.index(1)
    indice_2 = lista2.index(1)

    return indice_1, indice_2

lista_a = [3, 4, 5, 1]
lista_b = [1, 2, 3]

indice_1, indice_2 = retornar_tupla(lista_a, lista_b)

# print(type(retorno))
# print(retorno)

print(indice_1)
print(indice_2)