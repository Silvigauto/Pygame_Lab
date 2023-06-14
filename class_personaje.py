import pygame
from configuraciones import *


class Personaje:
    #atributos
    def __init__(self, tamaño:tuple, animaciones) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()

    #quieto - salta- camina_derecha_ camina_izquierda
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    #metodos
    def animar(self):
        pass

    def mover(self):
        pass

    def aplicar_gravedad(self):
        pass
    