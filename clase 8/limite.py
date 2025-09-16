def imprimir_numero(n: int)->None:

    if n > int(-991):
        imprimir_numero(n - 1)
    
    print(n)

imprimir_numero(0)