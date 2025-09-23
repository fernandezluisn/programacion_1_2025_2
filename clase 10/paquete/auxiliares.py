def recortar_lista(lista: list,
                   limite: any = False)->list:

    '''
    '''

    for i in range(len(lista)):
        if lista[i] == limite:
            indice_final = i
            break

    lista_retorno = lista[0: indice_final]

    return lista_retorno