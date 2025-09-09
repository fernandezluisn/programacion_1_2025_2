def buscar_maximo(cantidad_numeros: int = 5) -> int:

    '''
    '''

    for i in range(cantidad_numeros):

        numero_ingresado = int(input("Ingrese un número"))

        if i == 0: 
            maximo = numero_ingresado
        elif numero_ingresado > maximo:
            maximo = numero_ingresado

    return maximo

maximo_1 = buscar_maximo()

print("Búsqueda 2")

maximo_2 = buscar_maximo(3)

print(f"El máximo 1 es {maximo_1}")
print(f"El máximo 2 es {maximo_2}")



