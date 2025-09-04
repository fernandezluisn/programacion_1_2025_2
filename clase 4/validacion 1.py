clave = int(input("ingrese su clave"))
contador = 0


while clave != 619 and contador < 5:
    print("Esa no es la clave correcta")
    clave = int(input("ingrese su clave"))

    contador += 1

    if contador == 5:
        print("Ingresó demasiadas veces mal la clave, volver a intentar en ...")
        #Incluimos demora

#10 ** cantidad_caracteres de la clave
#37 ** cantidad_de_caracteres