def inicializar_matriz(n_filas: int,
                       p_columnas: int,
                       valor_por_defecto : any = False)->list:
    
    '''
    '''

    matriz = []

    for _ in range(n_filas):
        fila = [valor_por_defecto] * p_columnas

        matriz += [fila]

    return matriz

def mostrar_x_pantalla(lista_archivo: list)->None:

    for linea in lista_archivo:
        texto = linea.strip()

        for i in range(len(texto)):

            numero = ""
            contador = 0
            if 48 < ord(texto[i]) < 58:

                numero += texto[i]

            elif texto[i] == " ":
                contador += 1

                if contador % 2 == 0:
                    print(numero)
        