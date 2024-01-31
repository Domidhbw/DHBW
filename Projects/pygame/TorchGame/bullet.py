import pygame

BULLET_SPEED = 7


class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.direction = direction

    def updatePosition(self):
        self.rect.x += self.direction.x * BULLET_SPEED
        self.rect.y += self.direction.y * BULLET_SPEED