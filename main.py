import pygame, sys
from configuraciones import *
from pygame.locals import *


#pantalla
WIDTH = 1200
HEIGHT = 600
TAMAÑO_PANTALLA = (WIDTH,HEIGHT )
FPS = 18
RELOJ = pygame.time.Clock()
PANTALLA  = pygame.display.set_mode(TAMAÑO_PANTALLA)


fondo = pygame.image.load("Recursos\Fondos\campsite_by_dominique_van_velsen_deobxgw-fullview.jpg")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)
pygame.init()

#PERSONAJE

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina-izquierda"] = personaje_camina_izquierda


while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    

    PANTALLA.blit(fondo, (0,0))
    pygame.display.update()