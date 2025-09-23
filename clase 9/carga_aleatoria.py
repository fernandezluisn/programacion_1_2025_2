from paquete.funciones import *

lista_remeras = inicializar_lista(5)

seguir = "S"
while seguir == "S":

    print("La posición 0 es spiderman")
    print("La posición 1 es batman")
    print("La posición 2 es superman")
    print("La posición 3 es aquaman")
    print("La posición 4 es linterna verde")

    posicion = int(input("ingrese el indice que quiere modificar"))

    match posicion:
        case 0:
            nombre = "spiderman"
        case 1:
            nombre = "batman"
        case 2: 
            nombre = "superman"
        case 3:
            nombre = "aquaman"
        case 4:
            nombre = "linterna verde"

    lista_remeras[posicion] = input(f"ingrese cantidad de remeras de {nombre}")
    
    mostrar_lista(lista_remeras)

    seguir = input("Quiere realizar otra carga? S/N ")