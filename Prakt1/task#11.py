"""
Преобразование (обобщённых) координат квадрата на Python (задача #11)
Реализуйте графику на основе кода на языке C в Python. Нужно написать программу,
аналогичную написанной на C.
"""
import numpy as np
import matplotlib.pyplot as plt


class Origin:
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0


class Unit:
    def __init__(self, pixels):
        self.pixels = pixels


class RF:
    def __init__(self, x0, y0, scale_x, scale_y):
        self.O = Origin(x0, y0)
        self.UX = Unit(scale_x)
        self.UY = Unit(scale_y)


def get_X(rframe, x):
    scale_x = rframe.UX.pixels
    x0 = rframe.O.x0
    return scale_x * x + x0


def get_Y(rframe, y):
    scale_y = rframe.UY.pixels
    y0 = rframe.O.y0
    return -scale_y * y + y0


def draw_axes(rframe, x_min, x_max, y_min, y_max, color='black'):
    plt.axhline(0, color=color, linewidth=1)  # Ось X
    plt.axvline(0, color=color, linewidth=1)  # Ось Y
    plt.text(get_X(rframe, 0), get_Y(rframe, 0), "O", fontsize=12, ha='center')


def draw_polygon(rframe, xy):
    x_coords = [get_X(rframe, point[0]) for point in xy]
    y_coords = [get_Y(rframe, point[1]) for point in xy]

    # Закрываем многоугольник, повторяя первую точку
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])

    plt.plot(x_coords, y_coords, color='green')
    plt.fill(x_coords[:-1], y_coords[:-1], alpha=0.5)  # Заполняем многоугольник


def alloc_matrix_d(rows, cols):
    """Создает двумерную матрицу, заполненную нулями."""
    return np.zeros((rows, cols))


def delete_matrix_d(matrix):
    """Удаляет ссылку на матрицу. В Python память освобождается автоматически."""
    del matrix


def copy_matrix_d(src):
    """Копирует матрицу."""
    return np.copy(src)


def multiply_matrix_d(A, B):
    """Умножает две матрицы A и B и возвращает результат."""
    return np.dot(A, B)


def matrix_rotation_d(angle):
    """Создает матрицу поворота на заданный угол в радианах."""
    cs = np.cos(angle)
    sn = np.sin(angle)
    return np.array([[cs, -sn], [sn, cs]])


def type_matrix_d_sep(rows, cols, name):
    """Запрашивает ввод значений для матрицы и возвращает её."""
    print(f"Type matrix {name}[{rows}][{cols}]")
    M = alloc_matrix_d(rows, cols)
    for i in range(rows):
        for j in range(cols):
            value = float(input(f"Enter {name}[{i}][{j}]: "))
            M[i][j] = value
    return M


def print_matrix_d(M, name):
    """Выводит матрицу на экран."""
    print(f"----\n{name} = ")
    for row in M:
        print(" ".join(map(str, row)))


# Пример использования
if __name__ == "__main__":
    rframe = RF(x0=60, y0=450, scale_x=60, scale_y=60)

    plt.figure(figsize=(8, 6))
    plt.xlim(-5, 8)
    plt.ylim(-5, 7)

    draw_axes(rframe, 0.0, 8.0, 0.0, 7.0, color='green')

    N_points = 4
    N = 2

    # Запрашиваем ввод матрицы L
    L = type_matrix_d_sep(N_points, N, "L")
    print_matrix_d(L, "L")  # Выводим введенную матрицу

    Lo = alloc_matrix_d(N_points, N)

    p = 0.95
    q = 1 - p
    N_iterations = 10

    for k in range(1, N_iterations + 1):
        draw_polygon(rframe, L)

        # Вычисление новых координат для создания воронки
        for i in range(N_points):
            L[i][0] *= p  # Сжимаем по X
            L[i][1] *= q  # Сжимаем по Y

        # Копируем новые координаты в Lo
        Lo = copy_matrix_d(L)

        plt.plot()  # Обновляем график

    # Пример поворота
    angle = np.pi / 4  # 45 градусов
    rotation_matrix = matrix_rotation_d(angle)
    L_rotated = multiply_matrix_d(L, rotation_matrix)

    # Рисуем повёрнутый многоугольник
    draw_polygon(rframe, L_rotated)

    plt.pause(0.5)  # Задержка для просмотра
    plt.show()

    # Освобождение матриц (необязательно в Python)
    delete_matrix_d(L)
    delete_matrix_d(Lo)
