from paquete.matrices import *
from paquete.manipulacion_archivos import *

ejecutar = True

matriz = inicializar_matriz(2, 2, 0)

productos = ["Peras", "Sandías"]
depositos = ["Avellaneda", "Lanús"]

RUTA_ARCHIVO = "clase 20 archivos/archivos/ejemplo.txt"

while ejecutar:

    print("Acciones que puede ejecutar: ")

    print("1- cargar ventas.")

    print("2- mostrar historial de ventas.")

    print("3- mostrar historial de ventas como lista.")

    print("4- cargar historial de ventas en archivo línea por línea")

    print("5- cargar historial de ventas en archivo como lista")

    print("6- mostrar archivo mediante función")

    print("7- mostrar csv")


    print("9- Salir.")

    opcion = int(input("Marque la opción deseada: "))

    match opcion:

        case 1:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):

                    mensaje = f"Ingrese cantidad de {productos[i]}" 
                    mensaje_2 = f" vendidas en {depositos[j]}: "

                    matriz[i][j] = int(input(mensaje + mensaje_2))
        
        case 2:

            archivo = open(RUTA_ARCHIVO, "r+")#r+ permite lectura y escritura            

            texto = archivo.read()

            archivo.write("Perro")

            print(type(texto))

            print(texto)            

            archivo.close()

        case 3:

            archivo = open(RUTA_ARCHIVO)
            texto = archivo.readlines()

            print(type(texto))

            mostrar_x_pantalla(texto)

            archivo.close()
        
        case 4:
            archivo = open(RUTA_ARCHIVO, "w")

            for i in range(len(matriz)):
                for j in range(len(matriz[i])):

                    mensaje = f"Ingrese cantidad de {productos[i]}" 
                    mensaje_2 = f" vendidas en {depositos[j]}: "

                    matriz[i][j] = int(input(mensaje + mensaje_2))

            for linea in matriz:
                linea_texto = ""
                for i in range(len(linea)):
                    
                    if i == len(linea) - 1: 
                        linea_texto += str(linea[i]) + "\n"
                    else:
                        linea_texto += str(linea[i]) + ";"            
                
                print(linea_texto)
                archivo.write(linea_texto)
            archivo.close()

        case 5:
            archivo = open(RUTA_ARCHIVO, "w")

            for i in range(len(matriz)):
                for j in range(len(matriz[i])):

                    mensaje = f"Ingrese cantidad de {productos[i]}" 
                    mensaje_2 = f" vendidas en {depositos[j]}: "

                    matriz[i][j] = int(input(mensaje + mensaje_2))

            lista_guardar = []

            for linea in matriz:
                linea_texto = ""
                
                for i in range(len(linea)):
                    
                    if i == len(linea) - 1: 
                        linea_texto += str(linea[i]) + "\n"
                    else:
                        linea_texto += str(linea[i]) + ";"            
                
                lista_guardar += linea_texto

            print(lista_guardar)    
            archivo.writelines(lista_guardar)
            archivo.close()

        case 6:
            lectura_archivos(RUTA_ARCHIVO)
        
        case 7:

            leer_csv("clase 20 archivos/archivos/ventas.csv")

        case 9:
            ejecutar = False