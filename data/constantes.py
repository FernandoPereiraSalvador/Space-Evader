# Archivo con variables constantes

import pygame

# Definir constantes para el ancho y alto de la pantalla

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define el tiempo que hay entre un disparo y otro
TIEMPO_ENTRE_DISPAROS = 1500

# Color de fondo
COLOR_DIA = (135, 206, 250)
COLOR_NOCHE = (0, 0, 0)


# Texto que se muestra en el menú del juego.
MENU_TEXT = "Press P to start"

# Crea una ventana de juego con las dimensiones definidas.
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))