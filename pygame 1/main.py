import pygame
from graficos import *

pygame.init()

ancho_de_basto = pygame.image.load("pygame 1/imagenes/1 de basto.jpg")

ventana = pygame.display.set_mode((ANCHO, ALTO))

icono = pygame.transform.scale(ancho_de_basto,
                               (32, 32))

pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ancho_de_basto)

activo = True

while activo:

    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            print(f"código= {pygame.QUIT}")
            activo = False

    ventana.fill(VERDE)

    ventana.blit(icono,
                 (100, 100))
    
    ventana.blit(ancho_de_basto,
                 (400, 400))
    
    pygame.draw.rect(ventana,
                     BLANCO,
                     (150, 150, 500, 500))
    
       
    # pygame.draw.circle(ventana,
    #                    BLANCO,
    #                    (700, 500),
    #                    40)
    
    # pygame.draw.line(ventana,
    #                  NEGRO,
    #                  (30, 30), (700, 80),
    #                  5)
    
    pygame.display.update()

pygame.quit()


