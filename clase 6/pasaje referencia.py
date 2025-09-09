lista_ejemplo = [1, 2, 3]
print(f"id: {id(lista_ejemplo)}")
print(lista_ejemplo)

def sumar_lista(lista_suma: list, 
                suma: int = 2)-> list:

    '''
    En la documentación explicamos 1- qué hace la función,

    2- qué tipo de valores recibe la función
    
    3- qué tipo de valores devuelve
    '''

    for i in range(len(lista_suma)):
        lista_suma[i] += suma

    return lista_suma

print("Llamamos función")

lista_resultado = sumar_lista(lista_ejemplo)

print(lista_ejemplo)
print(lista_resultado)

print(f"id: {id(lista_ejemplo)}")
print(f"id: {id(lista_resultado)}")

