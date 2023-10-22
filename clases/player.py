# Importar el módulo pygame para gráficos y eventos
import os

import pygame

# Importar las constantes de teclas y configuración de transparencia
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    RLEACCEL,
)

# Importar las constantes de ancho y alto de la pantalla
from data.constantes import SCREEN_WIDTH, SCREEN_HEIGHT


# Definir la clase Player que representa al jugador en el juego
class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
        Constructor de la clase
        """

        # Llamar al constructor de la clase base (pygame.sprite.Sprite)
        super(Player, self).__init__()

        # Cargar la imagen del jugador y configurar la transparencia (color clave)
        self.surf = pygame.image.load(os.path.join("./resources", "jet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        # Obtener el rectángulo que representa al jugador
        self.rect = self.surf.get_rect()

        # Crear la puntuacion
        self.puntuacion = 0

    def update(self, pressed_keys):
        """
        Actualiza la posición del jugador en función de las teclas presionadas y
        asegura que el jugador permanezca dentro de los límites de la pantalla.

        :param pressed_keys: Conjunto de teclas presionadas
        :return: None
        """

        # Actualiza la posición del jugador en función de las teclas presionadas
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Mantener al jugador dentro de los límites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def aumentar_puntuacion(self):
        """
        Aumenta la puntuacion del jugador en 10 puntos

        :return: None
        """
        self.puntuacion += 10
