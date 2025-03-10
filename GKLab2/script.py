import pygame

# Inicjalizacja pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Figura: Okrąg i Kwadrat")

# Kolory
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Parametry figur
circle_radius = 150
square_size = 125
cx, cy = WIDTH // 2, HEIGHT // 2  # Środek ekranu

running = True
while running:
    screen.fill(WHITE)
    # Rysowanie okręgu
    pygame.draw.circle(screen, BLACK, (cx, cy), circle_radius)
    # Rysowanie kwadratu wewnątrz okręgu
    square_x = cx - square_size // 2
    square_y = cy - square_size // 2
    pygame.draw.rect(screen, YELLOW, (square_x, square_y, square_size, square_size))
    pygame.display.flip()
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()