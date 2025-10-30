from paquete.validaciones import *

cadena = "Programación 1"

for i in range(len(cadena)):

    if cadena[i] == "a":
        print(f"posición {i}")

cadena_2 = "123 \"cadena\""

print(cadena_2[5:])
print(cadena_2[:4])

cadena_3 = cadena + " " + cadena_2

print(cadena_3)

cadena_4 = "O" * 5

print(cadena_4)

#valores ascii

print(f"a = {ord("a")}")
print(f"A = {ord("A")}")

print("A" == "a")

print(comparar_letra("A", "a"))

nombre_1 = "Pedro"

nombre_2 = "pEDRO"

print(comparar_cadena(nombre_1, nombre_2))
