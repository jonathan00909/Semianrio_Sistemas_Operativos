import pygame
import sys
import threading
import os
import random

# Función para mover la primera imagen de izquierda a derecha
def move_image1():
    global x1
    while not exit_program:
        x1 += speed1
        if x1 > screen_width:
            x1 = 0
        pygame.time.delay(30)

# Función para mover la segunda imagen de arriba a abajo
def move_image2():
    global y2
    while not exit_program:
        y2 += speed2
        if y2 > screen_height:
            y2 = 0
        pygame.time.delay(30)

# Función para redimensionar una imagen
def resize_image(image, width, height):
    return pygame.transform.scale(image, (width, height))

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
screen_width = 1920
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movimiento de Imágenes")

# Obtén la ruta de la carpeta del proyecto
project_folder = os.path.dirname(__file__)

# Lista de imágenes en la carpeta del proyecto
image_files = [f for f in os.listdir(project_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Selecciona dos imágenes aleatorias
random_images = random.sample(image_files, 2)

# Carga las imágenes y redimensiona
image1 = resize_image(pygame.image.load(os.path.join(project_folder, random_images[0])), 800, 600)
image2 = resize_image(pygame.image.load(os.path.join(project_folder, random_images[1])), 800, 600)

# Obtén los rectángulos de las imágenes
image1_rect = image1.get_rect()
image2_rect = image2.get_rect()

# Configuración inicial de la posición de las imágenes
x1, y1 = 0, (screen_height - image1_rect.height) // 2
x2, y2 = (screen_width - image2_rect.width) // 2, 0

# Velocidades de movimiento
speed1 = 5
speed2 = 3

# Variable para controlar la terminación de los hilos y el programa
exit_program = False

# Crea dos hilos para el movimiento de las imágenes
thread1 = threading.Thread(target=move_image1, daemon=True)
thread2 = threading.Thread(target=move_image2, daemon=True)

# Inicia los hilos
thread1.start()
thread2.start()

clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit_program = True  # Establece la bandera de salida

    # Borra la pantalla
    screen.fill((0, 0, 0))

    # Dibuja las imágenes en las nuevas posiciones
    screen.blit(image1, (x1, y1))
    screen.blit(image2, (x2, y2))

    # Actualiza la pantalla
    pygame.display.update()

    clock.tick(30)  # Limita la velocidad del bucle a 30 FPS

# Espera a que los hilos terminen antes de cerrar Pygame
thread1.join()
thread2.join()

# Cierra Pygame
pygame.quit()
sys.exit()
