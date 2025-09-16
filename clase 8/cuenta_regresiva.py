numero = int(input("Ingrese un número para iniciar cuenta regresiva: "))

for i in range(numero, -1, -1):
    print(i)

def contar_regresivamente(n: int)->None:

    '''
    Cuenta regresivamente

    Recibe un número desde el que inicia la cuenta

    No retorna nada
    '''

    if n == (-1):
        print("Finalizó")
    else:
        print(n)
        contar_regresivamente(n - 1)

print("Ahora se aplica recursividad")

contar_regresivamente(10)