dinero_en_cuenta = int(input("Ingrese su salario: $"))

bandera = "Si"

while dinero_en_cuenta > 0 and bandera == "Si":
    
    gasto = int(input("Ingrese el gasto realizado: "))

    # controla si voy a realizar el gasto
    if (dinero_en_cuenta - gasto) < 0:
        print("Fondos insuficientes")
        
    else:
        dinero_en_cuenta -= gasto

    print(f"Usted tiene disponibles ${dinero_en_cuenta}")
    bandera = input("¿Quiere seguir gastando?: Si/No ")
    

print("Ya no puede realizar más gastos.")