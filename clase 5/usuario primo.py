numero_ejemplo = int(input("Ingrese un número para calcular si es primo: "))

limite = (numero_ejemplo // 2)
numero_primo = True

for numero in range(2, limite):

    print(numero)
        
    if (numero_ejemplo % numero) == 0:
            numero_primo = False
            break

if numero_primo == True:
    print(f"{numero_ejemplo} es primo")
else:
    print(f"{numero_ejemplo} no es primo")