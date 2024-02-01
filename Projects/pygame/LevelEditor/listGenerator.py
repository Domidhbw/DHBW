import pygame
from testLevel import *
from TileManager import TileManager

class LevelGenerator:
    def __init__(self) -> None:
        self.LevelData = level_map
        self.tileManager = TileManager()
        self.level = self.createLevel()
        self.shift = pygame.Vector2()

    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.shift.x = -3
        elif keys[pygame.K_a]:
            self.shift.x = 3
        else:
            self.shift.x = 0
        if keys[pygame.K_w]:
            self.shift.y = 3
        elif keys[pygame.K_s]:
            self.shift.y = -3
        else:
            self.shift.y = 0

    def createLevel(self):
        level = list()
        for rowIndex,row in enumerate(self.LevelData):
            for colIndex,cell in enumerate(row):
                if not cell == " " or cell == 'o':
                    level.append(self.tileManager.createTile(cell, colIndex * tilsize, rowIndex * tilsize))
        return level

    def drawLevel(self,surface):
        for tile in self.level:
            pygame.draw.rect(surface,tile.color,tile.rect,0)
            pygame.draw.rect(surface,'white',tile.rect,1)

    def updateTilesPosition(self):
        for tile in self.level:
            tile.rect.update(tile.rect.left + self.shift.x,tile.rect.top + self.shift.y,tile.rect.width,tile.rect.height)

    def update(self):
        self.getInput()
        self.updateTilesPosition()
    

