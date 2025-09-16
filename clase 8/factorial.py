# Factorial de 5
# 5!
# 5 * 4 * 3 * 2 * 1

factorial = int(input("Ingrese el número del que quiere calcular el factorial"))

# resultado = 1

# for i in range(factorial, 1, -1):
#     resultado *= i

# print(f"El factorial de {factorial} es {resultado}")

def calcular_factorial(n: int) -> int:

    if n == 1:
        resultado = 1
    else:
        resultado = n * calcular_factorial(n - 1)

    return resultado

resultado_ejemplo = calcular_factorial(factorial)

print(f"El factorial de {factorial} es {resultado_ejemplo}")