from .auxiliares import *

def calcular_interseccion(conjunto_1: list,
                          conjunto_2: list) -> list:
    
    '''
    Cálcula la intersección entre dos conjuntos

    Recibe dos conjuntos de números

    Retorna la intersección en forma de lista
    '''

    #Definimos tamaño de lista de retorno
    if len(conjunto_1) < len(conjunto_2):
        cantidad_retorno = len(conjunto_1)
    else:
        cantidad_retorno = len(conjunto_2)

    #creamos lista de retorno
    interseccion = [False] * cantidad_retorno


    #definimos contador para usar como índice
    z = 0

    #buscamos valores repetidos
    for i in range(len(conjunto_1)):

        for j in range(len(conjunto_2)):            

            if conjunto_1[i] == conjunto_2[j]:
                #Agregamos elemento a la intersección en caso de que coincida
                interseccion[z] = conjunto_1[i]
                
                # sumamos 1 al indice de la lista de retorno
                z += 1
                break

    lista_retorno = recortar_lista(interseccion)            
    return lista_retorno

def calcular_union(conjunto_1: list,
                   conjunto_2: list)-> list:
    
    '''
    '''

    cantidad = len(conjunto_1) + len(conjunto_2)

    lista_retorno = [False] * cantidad

    interseccion = calcular_interseccion(conjunto_1, 
                          conjunto_2)

    z = 0

    #Agregamos valores de la intersección
    for i in range(len(interseccion)):
        lista_retorno[z] = interseccion[i]
        z += 1

    for i in range(len(conjunto_1)):
        bandera = False
        
        for j in range(len(interseccion)):
            if conjunto_1[i] == interseccion[j]:
                bandera = True 
                break

        if bandera == False:
            lista_retorno[z] = conjunto_1[i]
            z += 1

    for i in range(len(conjunto_2)):
        bandera = False
        
        for j in range(len(interseccion)):
            if conjunto_2[i] == interseccion[j]:
                bandera = True 
                break

        if bandera == False:
            lista_retorno[z] = conjunto_2[i]
            z += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno

def calcular_union_optimizado(conjunto_1: list,
                              conjunto_2: list)->list:
    
    '''
    '''
    cantidad = len(conjunto_1) + len(conjunto_2)

    lista_retorno = [False] * cantidad

    z = 0

    for i in range(len(conjunto_1)):
        lista_retorno[z] = conjunto_1[i]
        z += 1

    for i in range(len(conjunto_2)):

        bandera = False

        for j in range(len(conjunto_1)):

            if conjunto_1[j] == conjunto_2[i]:
                bandera = True
                break
        
        if bandera == False:
            lista_retorno[z] = conjunto_2[i]
            z += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno

def calcular_diferencia(conjunto_1: list,
                        conjunto_2: list) -> list:
    
    '''
    '''

    diferencia = [False] * len(conjunto_1)

    z = 0

    for i in range(len(conjunto_1)):

        bandera = True

        for j in range(len(conjunto_2)):

            if conjunto_1[i] == conjunto_2[j]:
                bandera = False
                break
            
        if bandera == True:
            diferencia[z] = conjunto_1[i]
            z += 1

    lista_retorno = recortar_lista(diferencia)

    return lista_retorno