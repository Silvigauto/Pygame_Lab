import pygame, sys
from configuraciones import *
from pygame.locals import *
from class_personaje import *


def actualizar_pantalla(pantalla, un_personaje:Personaje, fondo):
    pantalla.blit(fondo, (0,0))
    #plataformas
    un_personaje.update(pantalla)

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
#eje x, y
posicion_incial = (50, 450)
tamaño = (75,85)



diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_incial, 5)


while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
    
    keys = pygame.key.get_pressed()
    #esto no va a dar siempre true ?
    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"
    
    actualizar_pantalla(PANTALLA, mi_personaje, fondo)
    pygame.display.update()