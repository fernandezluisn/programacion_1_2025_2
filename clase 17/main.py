union = [1, 2, 3]
lista_2 = [4, 5, 6]

j = 1

union += [lista_2[j]]
union.append(lista_2[j])

union.append([1, 2, 3])
union.append("Perro")

union.insert(2, 999)

union.extend((True, False))

union.remove(5)

elemento_extraido = union.pop(3)

print(union)
print(elemento_extraido)

indice = union.index(True, 2, 7)

print(f"El índice es {indice}")
union.clear()

print(union)

lista = [7, 2, 6, 5, 9, 1]
lista.sort()
print(lista)

lista_strings = ["Perro", "Gato", "Ratón", "avestrúz"]

lista_strings.sort()

print(lista_strings)

lista_strings.reverse()
print(lista_strings)
