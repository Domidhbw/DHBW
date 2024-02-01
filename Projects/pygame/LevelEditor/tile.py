import pygame

class Tile:
    def __init__(self,left,top,color,char) -> None:
        self.heigth = 64
        self.width = 64
        self.rect = pygame.rect.Rect(left,top,self.width,self.heigth)
        self.color = color
        self.char = char


