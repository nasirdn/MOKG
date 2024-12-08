"""
Вращайте треугольник
𝐿 = [[3, −1],
     [4, 1],
     [2, 1]]
на 90 градусов (𝜋/2) против часовой стрелки с помощью матрицы:
𝑇 = [[0, 1],
     [−1, 0]]
Перед преобразованиями умножьте искусственно матрицу отрезка 𝐿 на 100, чтобы
он и его преобразованная версия имели видимую длину в пикселях. Как и в
предыдущей задаче, смещайте оригинальный треугольник, чтобы он был виден на
экране (сохраняйте оригинальную матрицу координат в изначальной матрице 𝐿 !),
после преобразования матрицы 𝐿 сместите на такое же количество пикселей в
видимую область окна новый треугольник 𝐿.
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
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Вращение треугольника")

    # Исходный треугольник (умноженный на 100 для видимости)
    L = np.array([[3, -1],
                  [4, 1],
                  [2, 1]]) * 100

    # Матрица вращения T
    T = np.array([[0, 1],
                  [-1, 0]])

    # Смещение для видимости
    offset_x, offset_y = 400, 450

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