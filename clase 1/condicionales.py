edad = int(input("Ingrese su edad: "))



if edad < 0:
    print(f"La edad {edad} no es válida, ingrese una edad correcta")
elif edad < 6:
    jardin = input("Indique en qué jardín cursa")
    print("Es un niño")
elif edad < 14:
    colegio = input("Indique en qué escuela cursa")
    print("Es un adolescente") 


if edad < 0:    
    print(f"La edad {edad} no es válida, ingrese una edad correcta")
else:
    if edad < 6:
        jardin = input("Indique en qué jardín cursa")
        print("Es un niño")
    else:
        if edad < 14:
            colegio = input("Indique en qué escuela cursa")
            print("Es un adolescente") 