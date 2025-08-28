limite_diario = 1000

acumulador_gastos = 0

while acumulador_gastos < limite_diario:

    print(f"Lleva gastados ${acumulador_gastos}")

    gasto = int(input("Ingrese el gasto realizado: "))

    acumulador_gastos += gasto

print(f"Ya gastó ${acumulador_gastos} y excedió el limite")    
