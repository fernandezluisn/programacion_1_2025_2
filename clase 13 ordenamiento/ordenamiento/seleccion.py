def ordenar_x_seleccion(lista: list)-> list:

    '''
    Ubica iterativamente el menor valor en el índice más bajo.

    Recibe un listado.

    Retorna un listado.
    '''

    if type(lista) != list:
        print("El parámetro de la función debe ser una lista")
        return
    
    for i in range(len(lista) - 1):

        indice_menor = i

        print(f"iteración {i}")

        for j in range(i + 1, len(lista)):

            if lista[j] < lista[indice_menor]:
                indice_menor = j

        if indice_menor != i:
            menor = lista[indice_menor]
            lista[indice_menor] = lista[i]
            lista[i] = menor
            print(f"Intercambio posición {i} por {indice_menor}")

    return lista