import os
import pygame
from pygame.locals import (
    KEYDOWN,
    QUIT,
)
from clases.disparo import Disparo
from archivo_record import guardar_records, cargar_records
from clases.cloud import Cloud
from clases.player import Player
from clases.enemy import Enemy
from clases.record import Record
from data.constantes import SCREEN_WIDTH, SCREEN_HEIGHT, TIEMPO_ENTRE_DISPAROS, COLOR_DIA, COLOR_NOCHE, MENU_TEXT, screen

def ingresar_nombre():
    """
    Esta función muestra un mensaje en pantalla, solicita al usuario que ingrese su nombre
    y espera a que el usuario presione la tecla "ENTER" para finalizar la entrada del nombre.

    :return: l nombre ingresado por el usuario.
    """
    # Configuración inicial
    input_activo = True  # Bandera para controlar la entrada de texto
    nombre_temporal = ""  # Almacena el nombre

    while input_activo:
        # Captura los eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_activo = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre_temporal = nombre_temporal[:-1]
                elif len(nombre_temporal) < 7:
                    nombre_temporal += event.unicode

        # Establece el color de fondo
        screen.fill(COLOR_DIA)

        # Configura la fuente y muestra un mensaje en pantalla
        font = pygame.font.Font(None, 36)
        mensaje_texto = "¡Has conseguido un record!"
        mensaje_surface = font.render(mensaje_texto, True, (255, 255, 255))
        mensaje_rect = mensaje_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(mensaje_surface, mensaje_rect)

        # Muestra un mensaje para ingresar el nombre
        etiqueta_texto = font.render("Introduce tu nombre para registrarlo:", True, (255, 255, 255))
        etiqueta_rect = etiqueta_texto.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10))
        texto_nombre = font.render(nombre_temporal, True, (255, 255, 255))
        texto_rect = texto_nombre.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        screen.blit(etiqueta_texto, etiqueta_rect)
        screen.blit(texto_nombre, texto_rect)

        # Actualiza
        pygame.display.flip()

    return nombre_temporal


def mostrar_menu():
    """
    Muestra el menu
    :return:  None
    """

    # Cargar registros
    records = cargar_records()
    records.sort(key=lambda record: record.score, reverse=True)

    # Bandera para controlar la visibilidad del menú
    menu = True
    while menu:
        # Captura los eventos
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    menu = False
            elif event.type == QUIT:
                menu = False

        # Establece el color de fondo
        screen.fill(COLOR_DIA)

        # Muestra el texto del menú en pantalla
        screen.blit(menu_text_surface, menu_text_rect)

        # Calcula la altura total de los registros y la posición de inicio
        total_height = len(records) * 40
        start_y = (SCREEN_HEIGHT - total_height) // 2

        # Muestra los records en pantalla uno por uno
        for record in records:
            record_text_surface = menu_font.render(f"{record.nombre_player} : {record.score}", True, (255, 255, 255))
            record_text_rect = record_text_surface.get_rect(center=(SCREEN_WIDTH // 2, start_y + -75))
            screen.blit(record_text_surface, record_text_rect)
            start_y += 40

        # Muestra los sprites en pantalla, excepto el jugador
        for entity in all_sprites:
            if type(entity) != Player:
                screen.blit(entity.surf, entity.rect)

        # # Actualiza la pantalla para mostrar los cambios
        pygame.display.flip()


def mostrar_pantalla_game_over(hay_record, nivel):
    """
     Muestra una pantalla de game over.
    :param hay_record: Indica si se ha establecido un nuevo récord.
    :return: None
    """

    # Bandera para controlar la visibilidad de la pantall
    game_over = True
    while game_over:
        # Captura los eventos
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    game_over = False
            elif event.type == QUIT:
                game_over = False

        # Establecer el color de fondo
        screen.fill(COLOR_DIA)

        # Configura la fuente y muestra la puntuación final y el nivel alcanzado
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Puntuación final: {player.puntuacion}', True, (255, 255, 255))
        level_text = font.render(f'Nivel alcanzado: {nivel}', True, (255, 255, 255))
        instruccion = font.render('Haz clic en P para salir', True, (255, 255, 255))
        record_text = font.render('¡¡¡Felicidades, has conseguido un nuevo récord!!!', True, (255, 255, 255))

        # Si hay un récord, muestra un mensaje adicional
        if hay_record:
            screen.blit(record_text, (SCREEN_WIDTH // 2 - record_text.get_width() // 2, 100))

        # Muestra la puntuación final, el nivel alcanzado y la instrucción en pantalla
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))
        screen.blit(level_text, (SCREEN_WIDTH // 2 - level_text.get_width() // 2, 300))
        screen.blit(instruccion, (SCREEN_WIDTH // 2 - instruccion.get_width() // 2, 500))
        pygame.display.flip()


def actualizar_ventana(tiempo_transcurrido, tiempo_ultimo_disparo, all_sprites, player, fondo_actual, running):
    nivel = (player.puntuacion // 500) + 1

    # Cargamos los sonidos
    move_up_sound = pygame.mixer.Sound(os.path.join("resources", "Rising_putter.ogg"))
    move_down_sound = pygame.mixer.Sound(os.path.join("resources", "Falling_putter.ogg"))
    collision_sound = pygame.mixer.Sound(os.path.join("resources", "Collision.ogg"))

    # Captura los eventos
    for event in pygame.event.get():
        nivel = (player.puntuacion // 500) + 1
        intervalo = max(75 + (450 - 50 * nivel), 5)
        pygame.time.set_timer(ADDENEMY, intervalo)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                move_up_sound.stop()
                move_up_sound.play()
            elif event.key == pygame.K_DOWN:
                move_down_sound.stop()
                move_down_sound.play()
            if event.key == pygame.K_SPACE:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - tiempo_ultimo_disparo >= TIEMPO_ENTRE_DISPAROS:
                    disparo = Disparo(player.rect)
                    all_sprites.add(disparo)
                    tiempo_ultimo_disparo = tiempo_actual
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy(nivel)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    tiempo_transcurrido += clock.get_time()

    # Cambiar el fondo cada 20 s
    if tiempo_transcurrido >= 20000:
        tiempo_transcurrido = 0
        if fondo_actual == COLOR_DIA:
            fondo_actual = COLOR_NOCHE
        else:
            fondo_actual = COLOR_DIA

    clouds.update()
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update(player, all_sprites)

    # Establece el fondo
    screen.fill(fondo_actual)

    # Dibuja las nubes primero
    for entity in all_sprites:
        if isinstance(entity, Cloud):
            screen.blit(entity.surf, entity.rect)

    # Dibuja al jugador y otros sprites
    for entity in all_sprites:
        if not isinstance(entity, Cloud):
            screen.blit(entity.surf, entity.rect)
            if isinstance(entity, Disparo):
                entity.update()

    # Comprobar colisión del jugador con enemigos
    if pygame.sprite.spritecollideany(player, enemies):
        # Si es así, eliminar al jugador y detener el bucle
        collision_sound.stop()
        collision_sound.play()
        player.kill()
        running = False

    # Mostramos la puntuacion y el nivel actual en la parte superior izquierda
    font = pygame.font.Font(None, 36)
    puntuacion_text = font.render(f'Puntuación: {player.puntuacion}', True, (255, 255, 255))
    nivel_text = font.render(f'Nivel: {nivel}', True, (255, 255, 255))
    screen.blit(puntuacion_text, (10, 10))
    screen.blit(nivel_text, (250, 10))

    pygame.display.flip()
    clock.tick(30)

    return tiempo_transcurrido, tiempo_ultimo_disparo, running, nivel


def finalizar_juego(nivel_alcanzado):
    """
    Finaliza el juego y muestra la pantalla de game over
    :return:
    """

    # Cargar los registros
    records = cargar_records()
    records.sort(key=lambda record: record.score, reverse=True)

    # Inicializar una bandera para indicar si se ha establecido un nuevo récord.
    hay_record = None

    # Iterar a través de los records y comprobar si el jugador a marcado uno.
    for record in records:
        if player.puntuacion > record.score or len(records) < 5:
            nombre_jugador = ingresar_nombre()
            nuevo_record = Record(nombre_jugador, player.puntuacion)
            records.insert(records.index(record), nuevo_record)
            hay_record = True
            break

    # Si no existen records el jugador ha marcado uno
    if len(records) == 0:
        nombre = ingresar_nombre()
        nuevo_record = Record(nombre, player.puntuacion)
        records.append(nuevo_record)

    # Cogemos los 5 primeros y los guardamos
    records = records[:5]
    guardar_records(records)

    # Cerramos el juego y mostramos la ventana org
    pygame.init()
    mostrar_pantalla_game_over(hay_record, nivel_alcanzado)
    pygame.mixer.quit()
    pygame.quit()


# Color del fondo
fondo_actual = COLOR_DIA

# Inicialización de pygame y configuración de la fuente del menú
pygame.font.init()
menu_font = pygame.font.Font(None, 36)
menu_text_surface = menu_font.render(MENU_TEXT, True, (255, 255, 255))
menu_text_rect = menu_text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

# Nivel inicial del juego
nivel = 1

# Configuración del reloj del juego para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Inicialización del mezclador de sonido de pygame y carga de música de fondo
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources", "Apoxode_-_Electric_1.ogg"))
pygame.mixer.music.play(loops=-1)

# Inicialización de pygame (nuevamente) y configuración de eventos personalizados
pygame.init()
ADDENEMY = pygame.USEREVENT + 1

# Creación del jugador
player = Player()

# Creación de grupos de sprites para gestionar objetos en el juego
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Creación de un grupo de nubes y configuración de un evento para agregar nubes
clouds = pygame.sprite.Group()
ADD_CLOUD = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_CLOUD, 1000)

# Mostrar el menú inicial del juego
mostrar_menu()

# Inicialización de variables relacionadas con el tiempo y el estado del juego
tiempo_transcurrido = 0
tiempo_ultimo_disparo = 0
running = True

# Ciclo principal del juego
while running:
    # Llama a la función 'actualizar_ventana' para actualizar el juego y obtener valores actualizados
    tiempo_transcurrido, tiempo_ultimo_disparo, running, nivel = actualizar_ventana(
        tiempo_transcurrido, tiempo_ultimo_disparo, all_sprites, player, fondo_actual, running
    )

# Llama a la función 'finalizar_juego' para gestionar el final del juego y pasa el nivel como argumento
finalizar_juego(nivel)