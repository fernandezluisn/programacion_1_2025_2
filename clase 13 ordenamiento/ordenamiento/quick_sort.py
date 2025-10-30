def ordenar_veloz(lista: list)-> list:

    '''
    Ordena los elementos mediante "divide y vencerás" usando un pivote

    Recibe una lista

    Retorna una lista
    '''

    if type(lista) != list:
        print("Debe recibir una lista")
        return
    
    menores = []
    mayores = []
    iguales = []

    if len(lista) > 1:

        pivote = lista[0]

        for i in range(len(lista)):

            if lista[i] < pivote:
                menores += [lista[i]]
            elif lista[i] == pivote:
                iguales += [lista[i]]
            else:
                mayores += [lista[i]]
        
        return ordenar_veloz(menores) + iguales + ordenar_veloz(mayores)
    else:
        return lista

