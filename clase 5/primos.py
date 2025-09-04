#Muestro primos entre uno y mil
#Es divisible solo por sí mismo y por 1

inicio = int(input("Ingrese inicio: "))

fin = int(input("Ingrese fin: "))

salto = int(input("Ingrese salto entre números"))

for numero_ejemplo in range(inicio, fin, salto):

    limite = (numero_ejemplo // 2) + 1
    numero_primo = True

    for numero in range(2, limite):
        
        if (numero_ejemplo % numero) == 0:
            numero_primo = False
            break

    if numero_primo == True:
        print(f"{numero_ejemplo} es primo")
    
    