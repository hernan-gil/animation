import pygame
import random

# Configuración
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_SIZE = 32
FPS = 60
SPEED = 2  # Velocidad de desplazamiento (configurable)
NUM_IMAGES = 10
FONT_SIZE = 42  # Tamaño de la fuente
TEXT_COLOR = (255, 255, 255)  # Color blanco para el texto
TEXT_DURATION = 3  # Duración de cada línea de texto en segundos

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Animación de Imágenes")
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)  # Fuente predeterminada

# Cargar imágenes (agrega más rutas si es necesario)
image_paths = ["Bitcoin.svg.png", "ethereum.png", "solana.png","tether.png", "xrp.png", "doge.png", "bnb.png", "cardano.png", "polkadot.png", "avalanche.png", "hl.png"]
images = [pygame.transform.scale(pygame.image.load(path).convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)) for path in image_paths]

# Clase para manejar las imágenes
class MovingImage:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - IMAGE_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - IMAGE_SIZE)
        self.z = 0  # La "profundidad" que simula el movimiento hacia el espectador
        self.image = random.choice(images)

    def move(self):
        self.z += SPEED
        self.x += (self.x - SCREEN_WIDTH // 2) * SPEED / 500
        self.y += (self.y - SCREEN_HEIGHT // 2) * SPEED / 500

    def is_off_screen(self):
        return self.x < -IMAGE_SIZE or self.x > SCREEN_WIDTH + IMAGE_SIZE or self.y < -IMAGE_SIZE or self.y > SCREEN_HEIGHT + IMAGE_SIZE

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

# Crear un grupo de imágenes
moving_images = [MovingImage() for _ in range(NUM_IMAGES)]

# Texto para mostrar
text_lines = ["Bienvenido a la animación", "Disfruta de las imágenes en movimiento", "Gracias por mirar"]
current_text_index = 0
text_timer = 0

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar texto
    text_timer += clock.get_time() / 1000  # Convertir tiempo a segundos
    if text_timer >= TEXT_DURATION:
        text_timer = 0
        current_text_index += 1
        if current_text_index >= len(text_lines):
            current_text_index = 0  # Reinicia el texto si lo deseas

    # Actualizar imágenes
    for img in moving_images:
        img.move()
    
    # Eliminar imágenes que están fuera de la pantalla y agregar nuevas
    moving_images = [img for img in moving_images if not img.is_off_screen()]
    while len(moving_images) < NUM_IMAGES:
        moving_images.append(MovingImage())

    # Dibujar
    screen.fill((0, 0, 0))  # Fondo negro
    for img in moving_images:
        img.draw(screen)

    # Dibujar texto centrado
    if current_text_index < len(text_lines):
        text_surface = font.render(text_lines[current_text_index], True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
