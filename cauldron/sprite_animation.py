import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la imagen
sprite_sheet_path = "21Z_2105.w030.n002.49A.p15.49.jpg"
original_width = 8159
original_height = 2802
frames = 6
frame_width = int(original_width // frames)
frame_height = original_height

# Dimensiones de la pantalla
screen_width = 1890
screen_height = 1020
scale_width = int(screen_width // frames)  # Escalado para que se ajusten al ancho de la pantalla
print(f"Ancho de cada imagen: {scale_width}")
scale_height = int(scale_width * (original_height / frame_width))  # Mantener la proporción
print(f"Alto de cada imagen: {scale_height}")
# Configuración de la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Cargar la imagen del sprite y escalarla
sprite_sheet = pygame.image.load(sprite_sheet_path)
scaled_sprite_sheet = pygame.transform.scale(sprite_sheet, (screen_width, scale_height))

# Dividir la imagen en fotogramas
def get_frames():
    frame_list = []
    for i in range(frames):
        frame_rect = pygame.Rect(i * scale_width, 0, scale_width, scale_height)
        print(f"Frame {i} {frame_rect}")
        frame = scaled_sprite_sheet.subsurface(frame_rect)
        frame_list.append(frame)
    return frame_list

frames_list = get_frames()

# Variables para la animación
current_frame = 0
clock = pygame.time.Clock()
animation_speed = 1  # Duración de cada frame en segundos
frame_duration = int(animation_speed * 1000)  # Duración en milisegundos
time_since_last_frame = 0

# Bucle principal del juego
running = True
while running:
    dt = clock.tick(60)  # Mantener 60 FPS
    time_since_last_frame += dt

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cambiar al siguiente frame si es necesario
    if time_since_last_frame >= frame_duration:
        current_frame = (current_frame + 1) % frames
        time_since_last_frame = 0

    # Dibujar el frame actual
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    screen.blit(frames_list[current_frame], ((screen_width - scale_width) // 2, (screen_height - scale_height) // 2))
    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()
