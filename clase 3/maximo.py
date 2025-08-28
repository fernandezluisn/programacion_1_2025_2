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