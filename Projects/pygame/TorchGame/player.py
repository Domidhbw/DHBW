import pygame

class Player():
    def __init__(self) -> None:
        self.surface = pygame.display.get_surface()
        self.playerPos = pygame.Vector2(self.surface.get_width()/2, self.surface.get_height()/2)
        self.speed = 5
        self.rect = pygame.Rect(self.playerPos.x, self.playerPos.y, 55,55)
    
    def update(self):
        self.rect.center = self.playerPos
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.playerPos.y -= self.speed
        if keys[pygame.K_s]:
            self.playerPos.y += self.speed
        if keys[pygame.K_a]:
            self.playerPos.x -= self.speed
        if keys[pygame.K_d]:
            self.playerPos.x += self.speed

    def wallHit(self):
        ##Add Collision
        #https://www.metanetsoftware.com/technique/tutorialA.html
        pass