def ordenar_x_burbujeo(lista: list)-> list:

    '''
    Recorre una lista n-1 veces y ordena elementos adyacentes.
    
    Recibe una lista
    
    Retorna una lista.
    '''

    if type(lista) != list:
        print("El parámetro que recibe debe ser una lista")
        return
    
    n = len(lista)
    
    for i in range(n):

        print(f"Iteración {i}")

        intercambio = False

        for j in range(0, n - 1 - i):

            if lista[j] > lista[j + 1]:

                intercambio = True
                mayor = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = mayor

                print(f"{mayor} se cambió {lista[j + 1]}")
        
        if intercambio == False:
            break

    return lista