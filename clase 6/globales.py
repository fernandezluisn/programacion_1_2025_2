#variable global
numero_especial = 6

def dividir(divisor ,dividendo: int = 12)-> int:
    '''
    '''

    global numero_especial

    numero_div = numero_especial

    #modifico la variable global
    numero_especial -= 2

    return dividendo / numero_especial

def multiplicar(num_1:int) ->int:
    '''
    '''

    global numero_especial

    #modifico la variable global
    numero_especial += 3

    return num_1 * numero_especial

resultado_1 = dividir()
resultado_2 = dividir()
resultado_4 = dividir()

#La utilización de variables globales genera acoplamiento y puede llevar a errores

resultado_3 = multiplicar(4)

print(f"El resultado 1 es {resultado_1}")
print(f"El resultado 2 es {resultado_2}")
print(f"El resultado 3 es {resultado_3}")
print(f"El resultado 4 es {resultado_4}")