"""
Нарисуйте на экране спираль в виде улитки Паскаля, используя полярные координаты:
𝑟 = 𝑏 + 2 ⋅ 𝑎 ⋅ cos(𝜃)
𝑥 = 𝑟 ⋅ cos(𝜃), 𝑦 = 𝑟 ⋅ sin(𝜃)
"""

import numpy as np
import pygame
import sys


def draw_spiral(screen, a, b, num_points=1000):
    # Угол от 0 до 2*pi
    theta = np.linspace(0, 2 * np.pi, num_points)

    # Вычисление r
    r = b + 2 * a * np.cos(theta)

    # Преобразование в декартовы координаты
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Смещение для видимости
    offset_x, offset_y = 400, 300

    # Отрисовка спирали
    for i in range(num_points - 1):
        pygame.draw.line(screen, (0, 0, 255),
                         (x[i] + offset_x, y[i] + offset_y),
                         (x[i + 1] + offset_x, y[i + 1] + offset_y))


def main():
    # Инициализация Pygame
    pygame.init()

    # Определение размеров окна
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Спираль улитки Паскаля")

    # Задание параметров
    a = 50
    b = 50

    # Основной цикл Pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Заполнение фона
        screen.fill((255, 255, 255))

        # Отрисовка спирали
        draw_spiral(screen, a, b)

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()