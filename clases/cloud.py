# Importar el módulo pygame para gráficos y eventos
import os

import pygame

# Importar la biblioteca random para números aleatorios
import random

# Importar la constante RLEACCEL para configurar la transparencia de la imagen
from pygame.locals import RLEACCEL

# Importar las constantes de ancho y alto de la pantalla
from data.constantes import SCREEN_WIDTH, SCREEN_HEIGHT


# Definir la clase Cloud que representa nubes en el juego
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        """
        Constructor de la clase
        """
        # Llamar al constructor de la clase base (pygame.sprite.Sprite)
        super(Cloud, self).__init__()

        # Cargar la imagen de la nube y configurar la transparencia
        self.surf = pygame.image.load(os.path.join("./resources", "cloud.png")).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # Establecer la posición inicial de la nube de forma aleatoria
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )

    def update(self):
        """
        Actualiza la posición de la nube desplazándola hacia la izquierda y
        elimina la nube cuando cruza el borde izquierdo de la pantalla.

        :return: None
        """

        # Mover la nube
        self.rect.move_ip(-5, 0)

        # Comprobar si la nube ha cruzado el borde izquierdo de la pantalla
        if self.rect.right < 0:
            self.kill()
