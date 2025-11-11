def lectura_archivos(ruta: str)-> None:

    with open(ruta) as archivo:

        for linea in archivo:
            print(linea, end = "")            

def leer_csv(ruta: str)-> list:

    with open(ruta) as archivo:

        nombres_columnas = archivo.readline().strip().split(",")

        matriz_valores = []

        for linea in archivo:

            fila = []
            linea = linea.rstrip("\n")
            lista_valores = linea.split(",")

            for valor in lista_valores:

                if valor.isdigit():
                    fila.append(int(valor))
            
            matriz_valores.append(fila)
    
    print(nombres_columnas)
    print(matriz_valores)

