import pygame
import random

# Configuración
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_SIZE = 32
FPS = 60
SPEED = 2  # Velocidad de desplazamiento (configurable)
NUM_IMAGES = 10

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animación de Imágenes")
clock = pygame.time.Clock()

# Cargar imagen (asegúrate de reemplazar 'image.png' con la ruta correcta)
image_path = "Bitcoin.svg.png"
image = pygame.image.load(image_path).convert_alpha()
image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))

# Clase para manejar las imágenes
class MovingImage:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - IMAGE_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - IMAGE_SIZE)
        self.z = 0  # La "profundidad" que simula el movimiento hacia el espectador

    def move(self):
        self.z += SPEED
        self.x += (self.x - SCREEN_WIDTH // 2) * SPEED / 500
        self.y += (self.y - SCREEN_HEIGHT // 2) * SPEED / 500

    def is_off_screen(self):
        return self.x < -IMAGE_SIZE or self.x > SCREEN_WIDTH + IMAGE_SIZE or self.y < -IMAGE_SIZE or self.y > SCREEN_HEIGHT + IMAGE_SIZE

    def draw(self, surface):
        surface.blit(image, (int(self.x), int(self.y)))

# Crear un grupo de imágenes
images = [MovingImage() for _ in range(NUM_IMAGES)]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar imágenes
    for img in images:
        img.move()
    
    # Eliminar imágenes que están fuera de la pantalla y agregar nuevas
    images = [img for img in images if not img.is_off_screen()]
    while len(images) < NUM_IMAGES:
        images.append(MovingImage())

    # Dibujar
    screen.fill((0, 0, 0))  # Fondo negro
    for img in images:
        img.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()