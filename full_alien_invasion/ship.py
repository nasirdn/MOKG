import pygame
import os
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load(os.path.join('resources/ship.bmp'))
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

        # Атрибут для щита
        self.shield_active = False
        self.shield_start_time = None

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляем атрибут x, а не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

            # Проверяем, отключен ли щит
        if self.shield_active and self.shield_start_time:
            if pygame.time.get_ticks() - self.shield_start_time >= 10000:  # 10 секунд
                self.shield_active = False
                self.shield_start_time = None  # Сбрасываем время активации

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

        if self.shield_active:
            shield_rect = self.rect.inflate(10, 10)  # Увеличиваем размер рамки
            pygame.draw.rect(self.screen, (0, 255, 0), shield_rect, 2)  # Рисуем рамку щита

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)