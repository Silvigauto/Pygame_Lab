#creo las listas que componen los fotogramas que hacen la animacion
import pygame

def reescalar_imagenes(lista, tamaño):
    for i in range(len(lista)):
        lista[i] = pygame.transform.scale(lista[i], tamaño)

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def obtener_rectangulos(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    #la suma del top del bottom tiene que se mayor a la velocidad de caida para que no este la probabilidad
    #de que se caiga el personaje
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom-10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right-2, principal.top,2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario


personaje_quieto = [pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/2.png"),
                    pygame.image.load("Recursos/aladin/quieto/3.png"),
                    ]


personaje_camina = [pygame.image.load("Recursos/aladin/camina/4.png"),
                    pygame.image.load("Recursos/aladin/camina/5.png"),
                    pygame.image.load("Recursos/aladin/camina/6.png"),
                    pygame.image.load("Recursos/aladin/camina/7.png")]


personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)


personaje_salta = [pygame.image.load("Recursos/aladin/salta/0.png"),
                    pygame.image.load("Recursos/aladin/salta/10.png"),
                    pygame.image.load("Recursos/aladin/salta/11.png"),
                    pygame.image.load("Recursos/aladin/salta/16.png")]



