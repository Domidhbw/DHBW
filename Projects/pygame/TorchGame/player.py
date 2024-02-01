import pygame


class Player():
    def __init__(self) -> None:
        self.surface = pygame.display.get_surface()
        self.playerPos = pygame.Vector2(self.surface.get_width()/2, self.surface.get_height()/2)
        self.speed = 5
        self.rect = pygame.Rect(self.playerPos.x, self.playerPos.y, 55,55)
        self.direction = pygame.Vector2(0,0)

    
    def getInput(self):
        self.direction = pygame.Vector2(0,0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y  = -1
        elif keys[pygame.K_s]:
            self.direction.y  = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_a]:
            self.direction.x  = -1
        elif keys[pygame.K_d]:
            self.direction.x  = 1
        else:
            self.direction.x = 0

        if self.direction.x != 0 and self.direction.y != 0:
            self.direction.x = 0
    
    def updatePosition(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

