def mostrar_matriz(matriz: list)-> None:

    '''
    '''
    #i es el índice de las filas
    for i in range(len(matriz)):

        for j in range(len(matriz[i])):

            print(matriz[i][j], end= " ")
        print("")

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

def mostrar_columna(matriz: list,
                    columna: int)-> None:
    
    '''
    '''

    for i in range(len(matriz)):
        print(matriz[i][columna])

def mostrar_fila(matriz: list,
                indice_fila: int = 0)-> None:
    
    for j in range(len(matriz[indice_fila])):
        print(matriz[indice_fila][j])

def cargar_secuencial(matriz: list,
                      mensaje: str)-> list:

    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            print(f"Fila = {i}, Columna = {j}")
            valor = int(input(f"{mensaje}"))
            matriz[i][j] = valor
            print()
    
    return matriz

def cargar_distribuido(matriz: list,
                     mensaje: str)-> list:
    
    '''
    '''

    if type(matriz) != list:
        print("ERROR. ¡¡Debe ingresar una matriz!!")
        return None
    
    busqueda = "S"

    while busqueda == "S":

        fila = int(input("Ingrese fila: "))
        columna = int(input("Ingrese columna: "))
        valor = int(input(mensaje))
        matriz[fila][columna] = valor
        busqueda = input("Desea seguir cargando notas: S/N ")
    
    return matriz