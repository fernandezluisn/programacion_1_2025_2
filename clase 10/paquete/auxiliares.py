def recortar_lista(lista: list,
                   limite: any = False)->list:

    '''
    '''

    for i in range(len(lista)):
        if lista[i] == limite:
            indice_final = i
            break
    
    #No es valido en parcial
    #lista_retorno = lista[0: indice_final]

    lista_retorno = [0] * (indice_final)

    for i in range(len(lista_retorno)):
        lista_retorno[i] = lista[i]

    return lista_retorno