import pygame
from pygame import mixer
from graficos import *

pygame.init()

mixer.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))

imagen_vertical = pygame.Surface((50, 50))
imagen_vertical.fill(MOSTAZA)
rectangulo = imagen_vertical.get_rect()

imagen_2 = pygame.Surface((50, 50))
imagen_2.fill(ROJO)
rectangulo_2 = imagen_2.get_rect()

reloj = pygame.time.Clock()

color_pantalla = VERDE

#poner canción de fondo
mixer.music.load("pygame 2/recursos/sonidos/Balatro Main Theme.mp3")
#mixer.music.play()
#mixer.music.set_volume(0.5)

EVENTO_PROPIO = pygame.USEREVENT + 1
tiempo = 3000

nombre = ""

ejecutar = True

pygame.time.set_timer(EVENTO_PROPIO,
                      tiempo)

while ejecutar:

    reloj.tick(FPS)

    for evento in pygame.event.get():
        #print(evento)

        
        if evento.type == pygame.QUIT:
            print(f"código= {pygame.QUIT}")
            ejecutar = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                rectangulo.x -= 10
            elif evento.key == pygame.K_RIGHT:
                rectangulo.x += 10
            else:
                nombre += evento.unicode
                print(nombre)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = evento.pos
            print(posicion_mouse)
            rectangulo.x = posicion_mouse[0]
            rectangulo.y = posicion_mouse[1]
        elif evento.type == EVENTO_PROPIO:
            if color_pantalla == VERDE:
                color_pantalla = NEGRO
            else:
                color_pantalla = VERDE

    ventana.fill(color_pantalla)

    pygame.draw.rect(ventana,
                     BLANCO,
                     (150, 150, 500, 500),
                     15)
    
   
    ventana.blit(imagen_vertical, rectangulo)
    ventana.blit(imagen_2, rectangulo_2)

    # rectangulo.y += 1

    # rectangulo.x += 1

    if rectangulo.top == ALTO:
        rectangulo.y = -49

    if rectangulo.left == ANCHO:
        rectangulo.x = -49

    if rectangulo.colliderect(rectangulo_2):
        imagen_vertical.fill(AZUL)
    else:
        imagen_vertical.fill(MOSTAZA)

    if rectangulo.collidepoint(posicion_mouse):
        print("Estás en el punto x= 450, y = 5")

    pygame.display.flip()
    
    
pygame.quit()