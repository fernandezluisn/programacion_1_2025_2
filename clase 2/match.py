edad = int(input("Ingrese su edad: "))

tipo_de_socio: str = "No asignado"
if edad < 0:
    print(f"La edad {edad} no es válida, ingrese una edad correcta")
elif edad < 6:    
    tipo_de_socio = "niño"
elif edad < 14:
    tipo_de_socio = "adolescente"
elif edad < 60:
    tipo_de_socio = "adulto"
else: 
    tipo_de_socio = "veterano"

match tipo_de_socio:
    case "niño":
        print("La cuota es $100 al mes")
    case "adolescente":
        print("La cuota es $200 al mes")
    case "adulto":
        print("La cuota es de $300 al mes")
    case "veterano":
        print("La cuota es $50 al mes")
    case _:
        print("No se asignó tipo de socio")