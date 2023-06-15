import pygame
from configuraciones import *


class Personaje:
    #atributos
    def __init__(self, tamaño, animaciones, posicion_incial, velocidad) -> None:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        #gravedad
        #mientras mayor el numero mas de golpe cae
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #rectangulos
        #el pygame.rect es para q me reconozco que es el rectangulo xd
        rectangulo = pygame.Rect(self.animaciones["camina_derecha"][0].get_rect())
        rectangulo.x = posicion_incial[0]
        rectangulo.y = posicion_incial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0

    #quieto - salta- camina_derecha_ camina_izquierda
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    #metodos
    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
        

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def update(self, pantalla,piso):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad*-1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")
                
        self.aplicar_gravedad(pantalla, piso)

    def aplicar_gravedad(self, pantalla,piso):
        #salto
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
        #caida
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        #colisiones
        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top
