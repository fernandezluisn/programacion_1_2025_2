def ordenar_x_insercion(lista: list)-> list:

    '''
    '''

    for i in range(1, len(lista)):

        print(f"i = {i}")

        elemento_auxiliar = lista[i]

        j = i - 1

        while j >= 0 and elemento_auxiliar < lista[j]:

            lista[j + 1] = lista[j]

            j -= 1
        
        lista [j + 1] = elemento_auxiliar

    return lista