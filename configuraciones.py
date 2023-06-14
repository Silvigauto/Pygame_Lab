#creo las listas que componen los fotogramas que hacen la animacion
import pygame

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista, tamaño):
    for i in range(len(lista)):
        lista[i] = pygame.transform.scale(tamaño)
    




personaje_quieto = [pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/3.png")]


personaje_camina = [pygame.image.load("Recursos/aladin/camina/4.png"),
                    pygame.image.load("Recursos/aladin/camina/5.png"),
                    pygame.image.load("Recursos/aladin/camina/6.png"),
                    pygame.image.load("Recursos/aladin/camina/7.png")]


personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)


personaje_salta = [pygame.image.load("Recursos/aladin/salta/0.png"),
                    pygame.image.load("Recursos/aladin/salta/10.png"),
                    pygame.image.load("Recursos/aladin/salta/11.png"),
                    pygame.image.load("Recursos/aladin/salta/16.png")]



