def restar_2(num: int)-> int:

    '''
    '''

    return num - 2

objeto_funcion = restar_2

lista = [3, "Perro", restar_2]

resultado_1 = lista[2](6)

print(resultado_1)

print(objeto_funcion(5))

def accionar_funcion(num: int,
                     funcion: any):
    
    return funcion(num)

def retornar_funcion(distancia: int,
                     funcion_1: any,
                     funcion_2: any):
    
    if distancia < 5:
        return funcion_1
    else:
        return funcion_2
    
    

resultado_2 = accionar_funcion(99, restar_2)
print(f"El resultado de la función de orden superior es {resultado_2}")

def crear_boton(ancho: int,
          alto: int,
          color: tuple,
          texto: str,
          funcion: any):
    
    pass