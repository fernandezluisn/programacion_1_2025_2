contador = 0
seguir = "S"

while contador < 5 and seguir == "S":

    contador += 1

    print(contador)

    seguir = input("Quiere continuar? N/S")

    # se puede usar break, pero algoritmicamente no es necesario
    if seguir == "N":
        break