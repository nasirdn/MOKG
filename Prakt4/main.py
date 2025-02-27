from simple_game import SimpleGame

if __name__ == "__main__":
    game = SimpleGame()
    game.run()

"""
Было выполнено:
Задание 1. Базовая заготовка игры.
- Окно игры фиксированного размера.
- Персонаж, управляемый стрелками на клавиатуре.
- Несколько неподвижных объектов в игровом поле.
Задание 2. Ближний бой.
- Создание зоны атаки с помощью дополнительного прямоугольника (pygame.Rect).
- Проверка пересечения (colliderect) зоны атаки и объектов.
- Простое удаление или изменение состояния объектов при столкновении с зоной атаки
Задание 4. Ловушки
- Использование невидимых зон (прямоугольников) для определения активации ловушки.
- Анимация ловушки или её исчезновение после активации.
- Отображение визуального эффекта активации.
"""