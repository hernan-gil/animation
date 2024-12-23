import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Battle Animation")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Velocidades
shooter_speed = 5
evasive_speed_x = 3
evasive_speed_y = 2
bullet_speed = 7

# Cargar imágenes
shooter_image = pygame.image.load("shooter.png")
shooter_image = pygame.transform.scale(shooter_image, (50, 30))

evasive_image = pygame.image.load("evasive.png")
evasive_image = pygame.transform.scale(evasive_image, (50, 30))

explosion_image = pygame.image.load("explosion.png")
explosion_image = pygame.transform.scale(explosion_image, (50, 30))

# Dimensiones del disparo
bullet_width = 5
bullet_height = 15

# Posiciones iniciales
shooter_x = screen_width - 50
shooter_y = screen_height - 30 - 10

evasive_x = (screen_width - 50) // 2
evasive_y = 10

bullet_x = None
bullet_y = None
bullet_active = False

# Contador de impactos
hits = 0

# Reloj para controlar los FPS
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60)  # Mantener 60 FPS

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar posiciones
    # Nave disparadora (movimiento de derecha a izquierda)
    shooter_x -= shooter_speed
    if shooter_x < 0:
        shooter_x = screen_width - 50

    # Nave evasora (movimiento horizontal y vertical)
    evasive_x += evasive_speed_x
    evasive_y += evasive_speed_y

    if evasive_x + 50 > screen_width or evasive_x < 0:
        evasive_speed_x = -evasive_speed_x

    if evasive_y + 30 > screen_height // 2 or evasive_y < 0:
        evasive_speed_y = -evasive_speed_y

    # Disparo
    if not bullet_active:
        bullet_x = shooter_x + 25 - bullet_width // 2
        bullet_y = shooter_y
        bullet_active = True

    if bullet_active:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_active = False

    # Comprobar colisión
    collision_detected = False
    if (bullet_x is not None and
        bullet_y is not None and
        evasive_x < bullet_x < evasive_x + 50 and
        evasive_y < bullet_y < evasive_y + 30):
        bullet_active = False  # Reiniciar el disparo
        bullet_y = None  # Resetear posición del disparo
        collision_detected = True
        hits += 1

    # Dibujar todo
    screen.fill(BLACK)

    # Dibujar nave disparadora
    screen.blit(shooter_image, (shooter_x, shooter_y))

    # Dibujar explosión o nave evasora
    if collision_detected:
        screen.blit(explosion_image, (evasive_x, evasive_y))
        pygame.display.flip()
        pygame.time.delay(500)  # Mostrar la explosión por 0.5 segundos
        collision_detected = False

    screen.blit(evasive_image, (evasive_x, evasive_y))

    # Dibujar bala
    if bullet_active:
        pygame.draw.rect(screen, WHITE, (bullet_x, bullet_y, bullet_width, bullet_height))

    # Mostrar contador de impactos
    font = pygame.font.Font(None, 36)
    hits_text = font.render(f"Impactos: {hits}", True, WHITE)
    screen.blit(hits_text, (screen_width - 200, 10))

    # Actualizar pantalla
    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()
