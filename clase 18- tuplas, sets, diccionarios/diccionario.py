edad = int(input("Ingrese la edad del alumno: "))

ejemplo_diccionario = {
    "nombre": "Juan",
    "edad": edad,
    "apellido": "Perez"
}

otro_diccionario = {
    "edad": 23,
    "apellido": "Suarez",
    "nombre": "María"
}

print(ejemplo_diccionario["edad"])
print(otro_diccionario["edad"])

for key in otro_diccionario.keys():
    print(key)

for pas, valor in otro_diccionario.items():
    print(f"clave = {pas}")
    print(f"valor = {valor}")
    print("")