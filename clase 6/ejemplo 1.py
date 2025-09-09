bandera = True

ejecutar = True

print("Buscamos el valor máximo")
while ejecutar:
    
    numero = int(input("Ingrese un número: "))

    if bandera:
        maximo = numero
        bandera = False
    elif numero > maximo:
        maximo = numero

    respuesta = input("¿Quiere seguir ingresando notas?: Si/No ")

    if respuesta == "No":
        ejecutar = False

    
print(f"El máximo es {maximo}")

bandera = True

ejecutar = True

while ejecutar:
    
    numero = int(input("Ingrese un número: "))

    if bandera:
        maximo2 = numero
        bandera = False

    elif numero > maximo2:
        maximo2 = numero

    respuesta = input("¿Quiere seguir ingresando notas?: Si/No ")

    if respuesta == "No":
        ejecutar = False

print(f"El máximo 2 es {maximo2}")
