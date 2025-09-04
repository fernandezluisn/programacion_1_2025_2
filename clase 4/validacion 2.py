contador = 0
acumulador = 0
seguir = "S"

while seguir == "S":
    nota = int(input("Ingrese la nota del alumno"))

    # validación de rango
    while nota < 1 or nota > 10:
        print("Los valores permitidos son del 1 al 10")
        nota = int(input("Ingrese la nota del alumno"))

    contador += 1
    acumulador += nota

    promedio = acumulador / contador

    seguir = input("¿Quiere continuar agregando notas? S/N")

    #validando conjuntos
    while (seguir!= "S" and seguir != "N"
           and seguir != "s" and seguir != "n"):
        
        print("Solo es válido ingresar S o N")
        seguir = input("¿Quiere continuar agregando notas? S/N")

print(promedio)

