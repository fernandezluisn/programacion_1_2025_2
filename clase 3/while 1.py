condicion = True

sentencias_a_repetir = int(input("Ingrese la cantidad de veces que quiere que se ejecute el while: "))

while condicion:
    print("Se está ejecutando el while")

    sentencias_a_repetir -= 1
    
    if sentencias_a_repetir == 0:
        condicion = False
