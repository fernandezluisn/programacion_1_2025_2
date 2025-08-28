palabra: str = "Soy un string"

print(palabra)

# El interprete de python pasa por encima de la definición de tipo y funciona igual
palabra_2: str = 2

print(palabra_2 + 2)

palabra_3 = 9.67

print(palabra_3)

# es fundamental ser prolijo y respetar reglas de estilo por esta cuestión

numero_1: int = 2

print(id(palabra_2) == id(numero_1))

numero_1 += 1

print(id(palabra_2) == id(numero_1))

palabra_2 += 1

print(id(palabra_2) == id(numero_1))
