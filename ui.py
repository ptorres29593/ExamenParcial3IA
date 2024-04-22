import pygame
import random
import time
from evolutionary_algorithm import evolutionary_algorithm as ea

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir el color de los puntos, del texto y de las líneas
color = (255, 255, 255)  # Blanco
line_color = (255, 0, 0)  # Rojo

# Definir las coordenadas de los puntos
points = [(700, 44), (412, 359), (89, 141), (586, 175), (130, 208), (337, 86), (446, 296), (262, 7), (776, 384), (462, 473), (358, 179), (243, 279), (409, 541), (254, 179), (320, 227)]

# Asignar a cada punto una letra del alfabeto
letters = [chr(65 + i) for i in range(15)]  # 65 es el código ASCII para 'A'

# Crear una fuente para el texto
font = pygame.font.Font(None, 24)

# Bucle principal del juego
running = True
iterations = 0
while running and iterations < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellenar la pantalla de negro
    screen.fill((0, 0, 0))

    if iterations == 0:
        order , new_population, fitness = ea(100, 15, 10, [0])
    else:
        order, new_population, fitness = ea(100, 15, 10, new_population)

    # Dibujar los puntos, las letras y las líneas
    for i in range(len(order)):
        start = points[letters.index(order[i])]
        end = points[letters.index(order[(i + 1) % len(order)])]  # El último punto se une con el primero
        pygame.draw.line(screen, line_color, start, end, 2)

    for point, letter in zip(points, letters):
        pygame.draw.circle(screen, color, point, 5)
        text = font.render(letter, True, color)
        screen.blit(text, (point[0] - 10, point[1] + 20))  # Ajustar la posición del texto

        # Dibujar el número de iteraciones
        iteration_text = font.render("Iteración: " + str((iterations + 1)*10), True, color)
        screen.blit(iteration_text, (10, 10))  # Posición del texto de

        # Dibujar el fitness
        fitness_text = font.render("Fitness: " + str(fitness), True, color)
        screen.blit(fitness_text, (10, 30))

    # Actualizar la pantalla
    pygame.display.flip()

    # Mostrar la pantalla durante 3 segundos
    time.sleep(1)

    iterations += 1

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting = False

# Salir de Pygame
pygame.quit()
