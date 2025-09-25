def buscar_lineal(lista: list, buscado: int)->int:

    for i in range(len(lista)):

        if lista[i] == buscado:
            return i
        
    print("No se encuentra el elemento buscado")


#[3, 4, 5, 7, 9] buscamos 9
#[7, 9]
#[9]

#presuponemos vector ordenado
def buscar_bin(lista: list, buscado: int)-> int:

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None