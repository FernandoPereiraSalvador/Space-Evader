import pygame

from data.constantes import SCREEN_WIDTH


class Disparo(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        """
        Constructor de la clase
        :param player_rect: El rectángulo que representa la posición y dimensiones del jugador que dispara
        """
        super(Disparo, self).__init__()

        # Crear una superficie rectangular para representar el disparo
        self.surf = pygame.Surface((10, 5))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()

        # Establecer la posición inicial del disparo en el lado derecho del jugador
        self.rect.midleft = player_rect.midright

        # Establecer la velocidad del disparo
        self.speed = 5

        # Crear una hitbox basada en la superficie del disparo
        self.mask = pygame.mask.from_surface(self.surf)

    def update(self):
        """
        Actualiza la posición y elimina el objeto si sale de la pantalla (por el lado derecho).

        :return:
        """

        # Mover el disparo
        self.rect.move_ip(self.speed, 0)

        # Comprobar se ha salido por el lado derecho
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
