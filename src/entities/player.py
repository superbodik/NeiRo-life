import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Красный цвет для игрока
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= 20
        if keys[pygame.K_s]:
            self.rect.y += 20
        if keys[pygame.K_a]:
            self.rect.x -= 20
        if keys[pygame.K_d]:
            self.rect.x += 20