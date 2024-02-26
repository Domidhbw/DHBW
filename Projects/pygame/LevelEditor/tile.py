import pygame

class Tile:
    def __init__(self,left,top,imagePath,char) -> None:
        self.heigth = 64
        self.width = 64
        self.sprite = pygame.image.load(imagePath).convert_alpha()
        self.rect = pygame.rect.Rect(left,top,self.width,self.heigth)
        self.char = char



