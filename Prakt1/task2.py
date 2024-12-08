"""
Нарисуйте графические примитивы (pygame) — окружность, линии, текст —
различными цветами в окне программы.
"""

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Графические примитивы в Pygame")

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Шрифт для текста
font = pygame.font.Font(None, 36)

def main():
    # Основной цикл Pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Заполнение фона
        screen.fill(WHITE)

        # Рисование окружности (синий цвет)
        pygame.draw.circle(screen, BLUE, (400, 300), 100)

        # Рисование линий (красный и зеленый цвета)
        pygame.draw.line(screen, RED, (100, 100), (700, 100), 5)  # Горизонтальная линия
        pygame.draw.line(screen, GREEN, (100, 200), (700, 200), 5)  # Еще одна горизонтальная линия

        # Рисование текста (черный цвет)
        text_surface = font.render('Привет, Pygame!', True, BLACK)
        screen.blit(text_surface, (320, 50))

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()