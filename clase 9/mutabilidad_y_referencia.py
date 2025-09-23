def sumar_2(num: int)-> int:

    '''
    '''
    print(f"id antes de la suma {id(num)}")
    resultado = num + 2

    print(f"id después de la suma {id(resultado)}")

    return resultado

def sumar_lista(lista: list)->list:

    '''
    '''

    print(f"id antes de la suma {id(lista)}")
    lista[0] = lista[0] + 2

    print(f"id después de la suma {id(lista)}")

    return lista

# todo es por referencia

#Cuando trabajamos con inmutables, parece que es por valor,
#en realidad estamos cambiando la referencia
sumar_2(4)
sumar_lista([0, 2, 3])