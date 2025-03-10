import pygame
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transforms")

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


# Funkcja rysująca wielokąt
def create_polygon():
    num_of_vertices = 5
    points = []
    for i in range(num_of_vertices):
        x = int(150 * math.cos(i * 2 * math.pi / num_of_vertices))
        y = int(150 * math.sin(i * 2 * math.pi / num_of_vertices))
        points.append((x, y))
    return points


# Funkcja do rysowania wielokąta
def draw_polygon(points):
    pygame.draw.polygon(screen, RED, points)


# Funkcja do skalowania
def scale(shape, sx, sy):
    center_x = sum([p[0] for p in shape]) / len(shape)
    center_y = sum([p[1] for p in shape]) / len(shape)
    scaled_shape = []
    for point in shape:
        new_x = center_x + (point[0] - center_x) * sx
        new_y = center_y + (point[1] - center_y) * sy
        scaled_shape.append((new_x, new_y))
    return scaled_shape


# Funkcja do obrotu
def rotate(shape, angle):
    center_x = sum([p[0] for p in shape]) / len(shape)
    center_y = sum([p[1] for p in shape]) / len(shape)
    rotated_shape = []
    for point in shape:
        x = point[0] - center_x
        y = point[1] - center_y
        new_x = center_x + x * math.cos(angle) - y * math.sin(angle)
        new_y = center_y + x * math.sin(angle) + y * math.cos(angle)
        rotated_shape.append((new_x, new_y))
    return rotated_shape


# Funkcja do przesunięcia
def translate(shape, tx, ty):
    translated_shape = []
    for point in shape:
        translated_shape.append((point[0] + tx, point[1] + ty))
    return translated_shape


# Funkcja do wyśrodkowania
def center(shape):
    # Obliczanie środka wielokąta
    center_x = sum([p[0] for p in shape]) / len(shape)
    center_y = sum([p[1] for p in shape]) / len(shape)

    # Obliczanie przesunięcia na środek ekranu
    tx = WIDTH // 2 - center_x
    ty = HEIGHT // 2 - center_y

    # Przesuwamy wszystkie punkty, aby środek był na środku ekranu
    return translate(shape, tx, ty)


# Funkcja do rysowania
def draw_transform(transform_index):
    screen.fill(YELLOW)  # Wypełnia tło na żółto
    shape = create_polygon()

    # Wybór transformacji
    if transform_index == 1:
        shape = scale(shape, 0.5, 0.5)
    elif transform_index == 2:
        shape = rotate(shape, math.radians(30))
    elif transform_index == 3:
        shape = scale(shape, 0.5, 0.8)
        shape = rotate(shape, math.radians(180))
    elif transform_index == 4:
        shape = scale(shape, 1, 0.5)
        shape = translate(shape, 0, -150)
    elif transform_index == 5:
        shape = scale(shape, 1, 0.3)
        shape = translate(shape, 0, -900)
    elif transform_index == 6:
        shape = translate(shape, 100, 0)
        shape = rotate(shape, math.pi / 2)
    elif transform_index == 7:
        shape = scale(shape, 0.5, 1)
        shape = rotate(shape, math.pi)
    elif transform_index == 8:
        shape = rotate(shape, math.radians(30))
        shape = scale(shape, 1, 0.3)
        shape = translate(shape, 0, 200)
    elif transform_index == 9:
        shape = translate(shape, 100, 0)
        shape = scale(shape, 1, 0.5)
        shape = rotate(shape, math.pi)

    # Wyśrodkowanie na ekranie
    shape = center(shape)

    draw_polygon(shape)


# Funkcja główna
def main():
    clock = pygame.time.Clock()
    running = True
    transform_index = 0  # Domyślnie żadna transformacja

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Zmiana transformacji przy naciśnięciu klawisza (1-9)
                if event.key == pygame.K_1:
                    transform_index = 1
                elif event.key == pygame.K_2:
                    transform_index = 2
                elif event.key == pygame.K_3:
                    transform_index = 3
                elif event.key == pygame.K_4:
                    transform_index = 4
                elif event.key == pygame.K_5:
                    transform_index = 5
                elif event.key == pygame.K_6:
                    transform_index = 6
                elif event.key == pygame.K_7:
                    transform_index = 7
                elif event.key == pygame.K_8:
                    transform_index = 8
                elif event.key == pygame.K_9:
                    transform_index = 9
                elif event.key == pygame.K_0:
                    transform_index = 0  # Resetuje do braku transformacji

        draw_transform(transform_index)
        pygame.display.flip()
        clock.tick(30)  # Ograniczenie liczby klatek na sekundę

    pygame.quit()


if __name__ == "__main__":
    main()
