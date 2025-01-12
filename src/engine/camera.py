import pygame

class Camera:
    def __init__(self, width, height):
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.zoom_level = 1.0  # Начальный уровень масштабирования

    def apply(self, entity_rect):
        return pygame.Rect(
            (entity_rect.x - self.camera_rect.x) * self.zoom_level,
            (entity_rect.y - self.camera_rect.y) * self.zoom_level,
            entity_rect.width * self.zoom_level,
            entity_rect.height * self.zoom_level
        )

    def update(self, target_rect):
        x = -target_rect.x + int(pygame.display.get_surface().get_width() / 2 / self.zoom_level)
        y = -target_rect.y + int(pygame.display.get_surface().get_height() / 2 / self.zoom_level)

        # Ограничение движения камеры
        x = min(0, x)  # Left
        y = min(0, y)  # Top
        x = max(-(self.camera_rect.width - pygame.display.get_surface().get_width() / self.zoom_level), x)  # Right
        y = max(-(self.camera_rect.height - pygame.display.get_surface().get_height() / self.zoom_level), y)  # Bottom

        self.camera_rect.x = x
        self.camera_rect.y = y

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Колесико вверх (приближение)
                self.zoom_level = min(2.0, self.zoom_level + 0.1)
            elif event.button == 5:  # Колесико вниз (удаление)
                self.zoom_level = max(0.5, self.zoom_level - 0.1)

    def get_zoomed_dimensions(self):
        screen = pygame.display.get_surface()
        return (
            int(screen.get_width() / self.zoom_level),
            int(screen.get_height() / self.zoom_level)
        )