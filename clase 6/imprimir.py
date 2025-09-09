def mostrar_mensaje(mensaje: str)-> None:
    '''
    Muestra un mensaje por consola

    Recibe un string

    No retorna nada
    '''
    print(mensaje)

texto = input("Ingrese texto a mostrar")

print(texto)

#Genero objeto vacío
retorno_none = mostrar_mensaje(texto)

print(retorno_none)

#mensaje existe solo dentro del contexto de la función
print(mensaje)