bandera = False

ejecutar = True


while ejecutar:

    numero = int(input("Ingrese un número: "))

    if bandera == False:
        minimo = numero
        bandera = True
    elif numero < minimo:
        minimo = numero

    continuar = input("Quiere seguir: Si/No")

    if continuar == "No":
        ejecutar = False

print(f"El número minimo es {minimo}")