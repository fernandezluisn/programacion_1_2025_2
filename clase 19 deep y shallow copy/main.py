import copy

matematica = [["Pedro", "Perez", 33], 
           ["María", "Suarez", 21]]

progra_1 = matematica

progra_1[1][1] = "Gutierrez"

print(progra_1)
print(matematica)

print(f"id progra 1 = {id(progra_1)}")
print(f"id matemática = {id(matematica)}")

#Hacemos copia superficial

arquitectura = copy.copy(progra_1)

print(f"id arquitectura = {id(arquitectura)}")

print("Hacemos un cambio en la edad de pedro en la lista de matemática")
matematica[0][2] = 99

arquitectura.append(["José", "Cano", 25])

print(f"arquitectura: {arquitectura}")
print(f"matematica: {matematica}")
print(f"progra_1: {progra_1}")

print("")
print("")

#Hacer una copia profunda
print("DEEP COPY")

ingles = copy.deepcopy(arquitectura)

print(f"Ingles: {ingles}")

print("Hacemos una modificación en la copia profunda")
ingles[2][2] = 35
print(f"arquitectura: {arquitectura}")
print(f"Ingles: {ingles}")

print(id(ingles[2]))
print(id(arquitectura[2]))

for i, valor in enumerate(ingles[1]):
    print(i, " ", valor)

nombres = ["Jorge", "Nicolas", "Lucía"]
edades = [23, 24, 22]

for nombre, edad in zip(nombres, edades):
    print(nombre, ", edad: ", edad)   

for i in range(len(nombres)):

    print(nombres[i], ", edad: ", edades[i])