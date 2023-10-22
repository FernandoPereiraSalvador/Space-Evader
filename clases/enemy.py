# Importar random para números aleatorios
import os
import random

# Importar pygame para usar la clase Sprite
import pygame
from pygame import RLEACCEL
import pygame.sprite

# Importar las constantes de ancho y alto de la pantalla
from data.constantes import SCREEN_WIDTH, SCREEN_HEIGHT

# Definir el objeto Enemy extendiendo pygame.sprite.Sprite
from clases.disparo import Disparo


class Enemy(pygame.sprite.Sprite):
    def __init__(self, nivel):
        """
        Constructor de la clase
        """

        # Llamar al constructor de la clase base (pygame.sprite.Sprite)
        super(Enemy, self).__init__()

        # Cargar la imagen del enemigo y configurar la transparencia
        self.surf = pygame.image.load(os.path.join("./resources", "missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        # Crear la máscara de colisión
        self.mask = pygame.mask.from_surface(self.surf)

        # Establecer la posición inicial del enemigo de forma aleatoria
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        # Establecer la velocidad del enemigo de forma aleatoria
        self.speed = max(random.randint(4 * nivel, 10 + 3 * nivel), 5)

    def update(self, player, group_sprites):
        """
        Actualiza la posición del sprite en función de su velocidad y elimina el sprite
        cuando cruza el borde izquierdo de la pantalla.

        :return: None
        """
        self.rect.move_ip(-self.speed, 0)

        # Comprobar si el sprite ha cruzado el borde izquierdo de la pantalla
        if self.rect.right < 0:
            self.kill()
            player.aumentar_puntuacion()

        # Almacenamos todos los disparos que hay en el juego
        sprites_disparos = pygame.sprite.Group()
        for sprite in group_sprites:
            if isinstance(sprite, Disparo):
                sprites_disparos.add(sprite)

        # Detectar colisiones
        colisiones = pygame.sprite.spritecollide(self, sprites_disparos, True, pygame.sprite.collide_mask)

        # Comprobar si se produjeron colisiones
        if colisiones:
            self.kill()
            player.aumentar_puntuacion()
