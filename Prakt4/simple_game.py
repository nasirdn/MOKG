import pygame
import random

class SimpleGame:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()

        # Константы
        self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 60
        self.PLAYER_SIZE = 50
        self.PLAYER_SPEED = 5
        self.OBJECT_SIZE = 50
        self.SPAWN_INTERVAL = 1000  # Интервал появления врагов в миллисекундах
        self.ATTACK_RANGE = 70  # Радиус зоны атаки
        self.TRAP_SIZE = 40  # Размер ловушки
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)  # Цвет для ловушек

        # Настройка окна игры
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Простая 2D Игра с Ловушками")
        self.clock = pygame.time.Clock()

        # Состояние игры
        self.reset_game()

    def reset_game(self):
        self.player_pos = [self.WIDTH // 2, self.HEIGHT // 2]
        self.player_health = 100  # Здоровье игрока
        self.enemies = []
        self.traps = []
        self.last_spawn_time = pygame.time.get_ticks()
        self.last_trap_time = pygame.time.get_ticks()

    def get_valid_starting_position(self):
        while True:
            pos = [random.randint(0, self.WIDTH - self.OBJECT_SIZE), random.randint(0, self.HEIGHT - self.OBJECT_SIZE)]
            if all(not pygame.Rect(pos[0], pos[1], self.OBJECT_SIZE, self.OBJECT_SIZE).colliderect(pygame.Rect(enemy)) for enemy in self.enemies):
                return pos

    def spawn_enemy(self):
        if len(self.enemies) < 10:
            pos = self.get_valid_starting_position()
            self.enemies.append(pygame.Rect(pos[0], pos[1], self.OBJECT_SIZE, self.OBJECT_SIZE))

    def create_trap(self):
        pos = [random.randint(0, self.WIDTH - self.TRAP_SIZE), random.randint(0, self.HEIGHT - self.TRAP_SIZE)]
        self.traps.append(pygame.Rect(pos[0], pos[1], self.TRAP_SIZE, self.TRAP_SIZE))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:  # Проверка нажатия клавиши Q для выхода
                pygame.quit()
                return

            if keys[pygame.K_LEFT]:
                self.player_pos[0] -= self.PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.player_pos[0] += self.PLAYER_SPEED
            if keys[pygame.K_UP]:
                self.player_pos[1] -= self.PLAYER_SPEED
            if keys[pygame.K_DOWN]:
                self.player_pos[1] += self.PLAYER_SPEED

            # Ограничение движения персонажа
            self.player_pos[0] = max(5, min(self.WIDTH - self.PLAYER_SIZE - 5, self.player_pos[0]))
            self.player_pos[1] = max(5, min(self.HEIGHT - self.PLAYER_SIZE - 5, self.player_pos[1]))

            # Проверка нажатия клавиши атаки
            if keys[pygame.K_SPACE]:
                attack_zone = pygame.Rect(self.player_pos[0] - self.ATTACK_RANGE // 2, self.player_pos[1] - self.ATTACK_RANGE // 2, self.ATTACK_RANGE, self.ATTACK_RANGE)
                # Удаление врагов, попавших в зону атаки
                self.enemies = [enemy for enemy in self.enemies if not enemy.colliderect(attack_zone)]

            # Проверка на попадание в ловушки
            player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], self.PLAYER_SIZE, self.PLAYER_SIZE)
            for trap in self.traps:
                if player_rect.colliderect(trap):
                    self.player_health -= 10  # Наносим урон игроку
                    self.traps.remove(trap)  # Удаляем ловушку после активации

            # Проверка здоровья игрока
            if self.player_health <= 0:
                self.reset_game()  # Сброс игры, если здоровье игрока 0

            # Периодическое появление врагов
            current_time = pygame.time.get_ticks()
            if current_time - self.last_spawn_time > self.SPAWN_INTERVAL:
                self.spawn_enemy()
                self.last_spawn_time = current_time

            # Периодическое создание ловушек
            if current_time - self.last_trap_time > 3000:  # Каждые 3 секунды
                self.create_trap()
                self.last_trap_time = current_time

            # Рендеринг
            self.screen.fill(self.WHITE)
            pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.WIDTH, self.HEIGHT), 5)  # Стены
            pygame.draw.rect(self.screen, self.BLUE, (self.player_pos[0], self.player_pos[1], self.PLAYER_SIZE, self.PLAYER_SIZE))  # Персонаж

            # Отрисовка врагов
            for enemy in self.enemies:
                pygame.draw.rect(self.screen, self.RED, enemy)

            # Отрисовка ловушек
            for trap in self.traps:
                pygame.draw.rect(self.screen, self.YELLOW, trap)

            # Отрисовка зоны атаки, если она активна
            if keys[pygame.K_SPACE]:
                pygame.draw.rect(self.screen, self.GREEN, attack_zone, 2)

            # Отображение здоровья игрока
            health_text = f"Health: {self.player_health}"
            font = pygame.font.Font(None, 36)
            text_surface = font.render(health_text, True, self.BLACK)
            self.screen.blit(text_surface, (10, 10))

            # Обновление экрана
            pygame.display.flip()
            self.clock.tick(self.FPS)
