import pygame
import random
import os
from pygame.sprite import Sprite


class Bonus(Sprite):
    """Класс для представления бонуса."""

    def __init__(self, ai_game, bonus_type):
        """Инициализирует бонус и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bonus_type = bonus_type

        # Загрузка изображения бонуса в зависимости от типа
        if self.bonus_type == 'life':
            self.image = pygame.image.load(os.path.join('resources/life.bmp'))
        elif self.bonus_type == 'shield':
            self.image = pygame.image.load(os.path.join('resources/shield.bmp'))
        elif self.bonus_type == 'power':
            self.image = pygame.image.load(os.path.join('resources/powerup.bmp'))

        self.rect = self.image.get_rect()

        # Позиция бонуса
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0  # Начальная позиция вверху экрана

        self.speed = 1  # Скорость падения бонуса

    def update(self):
        """Обновляет позицию бонуса."""
        self.rect.y += self.speed

    def draw_bonus(self):
        """Выводит бонус на экране."""
        self.screen.blit(self.image, self.rect)
