def inicializar_lista(cantidad_elementos: int,
                      valor_por_defecto: any = 0)-> list:
    
    return [valor_por_defecto] * cantidad_elementos

def mostrar_lista(lista: list)-> None:
    '''
    '''
    
    for i in range(len(lista)):
        print(lista[i], end = "-")

def cargar_lista(lista: list,
                 mensaje: str)-> list:

    '''
    '''

    if type(lista) != list:
        print("ERROR. La función solo permite listas")
        return None

    for i in range(len(lista)):
        print(f"posición {i}", end=": ")
        lista[i] = input(mensaje)

    #return lista


    
