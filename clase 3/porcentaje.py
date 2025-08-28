cantidad_encuestas = int(input("Ingrese cantidad de encuestas: "))

contador_a = 0
contador_b = 0

while (contador_a + contador_b) < cantidad_encuestas:

    producto = input("¿qué producto prefiere? a o b")

    if producto == "a":
        contador_a += 1
    elif producto == "b":
        contador_b += 1
    else:
        print("Solo puede ingresar a o b")

print(f"El {contador_a / cantidad_encuestas * 100}% prefiere el producto A")
print(f"El {contador_b / cantidad_encuestas * 100}% prefiere el producto B")