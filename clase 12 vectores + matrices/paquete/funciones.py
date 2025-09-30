def buscar_texto(texto: str, 
                lista_strings: list) -> int:
    
    '''
    
    '''
    
    for i in range(len(lista_strings)):

        if lista_strings[i] == texto:
            return i
        
    