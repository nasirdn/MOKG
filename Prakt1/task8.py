"""
Отразите треугольник
𝐿 = [[8, 1],
     [7, 3],
     [6, 2]]
относительно линии 𝑦 = 𝑥 с помощью матрицы:
𝑇 = [[0, 1],
     [1, 0]]
Также прибегайте к смещениям в пикселях, к умножению на 100 и тому подобным
приёмам, как и в предыдущей задаче, чтобы треугольники были видны.
"""

import numpy as np
import pygame
import sys


def transform_triangle(triangle, transformation_matrix):
    # Применение матричного преобразования к вершинам треугольника
    new_vertices = []
    for vertex in triangle:
        new_vertex = transformation_matrix @ vertex
        new_vertices.append(new_vertex)
    return np.array(new_vertices)


def main():
    # Инициализация Pygame
    pygame.init()

    # Определение размеров окна
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Отражение треугольника")

    # Исходный треугольник (умноженный на 100 для видимости)
    L = np.array([[8, 1],
                  [7, 3],
                  [6, 2]]) * 100

    # Матрица отражения относительно линии y = x
    T = np.array([[0, 1],
                  [1, 0]])

    # Смещение для видимости
    offset_x, offset_y = -75, -90

    # Преобразование треугольника
    L_transformed = transform_triangle(L, T) + np.array([offset_x, offset_y])

    # Смещение оригинального треугольника
    L = L + np.array([offset_x, offset_y])

    # Основной цикл Pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Заполнение фона
        screen.fill((255, 255, 255))

        # Отрисовка оригинального треугольника (красный цвет)
        pygame.draw.polygon(screen, (255, 0, 0), L)

        # Отрисовка преобразованного треугольника (синий цвет)
        pygame.draw.polygon(screen, (0, 0, 255), L_transformed)

        # Отрисовка осей
        pygame.draw.line(screen, (0, 0, 0), (0, height // 2), (width, height // 2), 2)  # Ось X
        pygame.draw.line(screen, (0, 0, 0), (width // 2, 0), (width // 2, height), 2)  # Ось Y

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()