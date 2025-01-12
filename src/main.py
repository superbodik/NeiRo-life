import sys
import os
import pygame
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import sys
from src.engine.world_generator import WorldGenerator
from src.engine.camera import Camera
from src.entities.player import Player

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("NeiRo-World")

# Создание мира
world_width = SCREEN_WIDTH // TILE_SIZE * 10  # Увеличиваем мир в 10 раз
world_height = SCREEN_HEIGHT // TILE_SIZE * 10  # Увеличиваем мир в 10 раз
world_generator = WorldGenerator(world_width, world_height)

# Начальная позиция камеры
camera = Camera(world_width * TILE_SIZE, world_height * TILE_SIZE)

# Создание игрока
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Изменение размера окна
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            camera.handle_event(event)

    # Обработка ввода
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Заливка экрана цветом (например, черным)
    screen.fill((0, 0, 0))

    # Рендеринг видимых тайлов
    visible_tiles = world_generator.get_visible_tiles(camera.camera_rect, camera.zoom_level, TILE_SIZE)
    for x, y, tile in visible_tiles:
        if tile is not None:
            color = {
                'water': (0, 0, 255),
                'grass': (0, 255, 0),
                'mountain': (128, 128, 128)
            }[tile]

            screen_x = (x * TILE_SIZE - camera.camera_rect.x) * camera.zoom_level
            screen_y = (y * TILE_SIZE - camera.camera_rect.y) * camera.zoom_level

            pygame.draw.rect(
                screen,
                color,
                (screen_x, screen_y, int(TILE_SIZE * camera.zoom_level), int(TILE_SIZE * camera.zoom_level))
            )

    # Рендеринг игрока
    player_screen_pos = camera.apply(player.rect)
    screen.blit(player.image, player_screen_pos.topleft)

    # Обновление камеры
    camera.update(player.rect)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()