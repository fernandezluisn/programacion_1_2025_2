def validar_mayuscula(caracter: str)-> bool:

    '''
    '''

    es_mayus = False

    if 64 < ord(caracter) < 91:
        es_mayus = True

    return es_mayus



def comparar_letra(caracter_1: str, caracter_2:str)-> bool:

    '''
    '''

    es_igual = False

    diferencia = ord(caracter_1) - ord(caracter_2)
    
    if (caracter_1 == caracter_2 
        or diferencia == 32 
        or diferencia == -32):

        es_igual = True

    
    return es_igual

def comparar_cadena(cadena_1: str, cadena_2: str)-> bool:

    '''
    '''

    son_iguales = True

    if len(cadena_1) != len(cadena_2):
        return False
    
    for i in range(len(cadena_1)):

        if comparar_letra(cadena_1[i], cadena_2[i]) == False:
            son_iguales = False
            break

    return son_iguales