ejemplo_set = {4, 3, 1, 4, 2, 5, 6, 3, 1}
ejemplo_2_set = {7, 8, 9, 1, 4}

print(f"set 1 = {ejemplo_set}")
print(f"set 2 = {ejemplo_2_set}")

union_set = ejemplo_set.union(ejemplo_2_set)

print(f"unión = {union_set}")

diferencia = ejemplo_set - ejemplo_2_set

print(f"diferencia = {diferencia}")

disyuncion = ejemplo_2_set | ejemplo_set

print(f"disyunción = {disyuncion}")

dif_simetrica = ejemplo_set.symmetric_difference(ejemplo_2_set)

print(f"diferencia simetrica = {dif_simetrica}")

dif = ejemplo_set.difference(ejemplo_2_set)

print(f"diferencia2 = {dif}")

interseccion = ejemplo_set.intersection(ejemplo_2_set)
print(f"intersección = {interseccion}")
