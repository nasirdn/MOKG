"""
Постройте квадрат, масштабируйте его с коэффициентом 𝑚 = 0.9 и поворачивайте на угол 𝛼 = 𝜋/32. Начальные координаты квадрата:
𝑋 = [[2, −2],
     [−2, −2],
     [−2, 2],
     [2, 2]] × 100
Используйте комбинированное преобразование и выполните 20 таких операций с
отрисовкой в pygame.
"""

import numpy as np
import pygame
import sys


def rotate_matrix(angle):
    """Создает матрицу поворота на заданный угол."""
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])


def scale_matrix(scale_factor):
    """Создает матрицу масштабирования с заданным коэффициентом."""
    return np.array([[scale_factor, 0],
                     [0, scale_factor]])


def transform_square(square, scale_factor, angle):
    """Применяет комбинированное преобразование (масштабирование и поворот) к квадрату."""
    # Масштабирование
    scale = scale_matrix(scale_factor)
    scaled_square = square @ scale

    # Поворот
    rotation = rotate_matrix(angle)
    transformed_square = scaled_square @ rotation

    return transformed_square


def main():
    # Инициализация Pygame
    pygame.init()

    # Определение размеров окна
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Преобразование квадрата")

    # Начальные координаты квадрата (умноженные на 100 для видимости)
    square = np.array([[2, -2],
                       [-2, -2],
                       [-2, 2],
                       [2, 2]]) * 100

    # Параметры трансформации
    scale_factor = 0.9
    angle = np.pi / 32

    # Смещение для видимости
    offset_x, offset_y = width // 2, height // 2

    # Основной цикл Pygame
    running = True
    iterations = 20
    for i in range(iterations):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Заполнение фона
        screen.fill((255, 255, 255))

        # Применение преобразования
        square = transform_square(square, scale_factor, angle)

        # Смещение для отрисовки
        square_transformed = square + np.array([offset_x, offset_y])

        # Отрисовка квадрата
        pygame.draw.polygon(screen, (0, 0, 255), square_transformed)

        # Обновление экрана
        pygame.display.flip()
        pygame.time.delay(500)  # Задержка для визуализации

    # Завершение Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()