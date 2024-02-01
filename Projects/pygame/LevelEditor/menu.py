import pygame
from testLevel import *
from TileManager import TileManager

class selectMenu:
    def __init__(self) -> None:
        self.selectedItems = [0,3]
        self.tiles = list()
        self.upRect = pygame.rect.Rect(1120,50,60,50)
        self.upButton = [[1120,100],[1150,50],[1180,100]]
        self.downRect = pygame.rect.Rect(1120,500,60,50)
        self.downButton = [[1120,500],[1150,550],[1180,500]]
        self.activeTile = 'x'
        self.tileManager = TileManager()
        self.createTilesAndAssignThemToList()
        self.activeTiles = self.tiles[self.selectedItems[0]:self.selectedItems[1]]
        self.menuBackground = pygame.rect.Rect((1100,0,100,600))

    def drawMenu(self,screen):
        pygame.draw.rect(screen,'red',self.menuBackground)
        pygame.draw.polygon(screen, (0, 255, 255), self.upButton)
        pygame.draw.polygon(screen, (0, 255, 255), self.downButton)

    def createTilesAndAssignThemToList(self):
        chars = list(tiles.keys())
        for char in chars:
            self.tiles.append(self.tileManager.createTile(char,0,0))
        
    def drawTheTilesOnTheMenu(self,surface):
        x = 1110
        y = 200
        for tile in self.activeTiles:
            tile.rect.x = x
            tile.rect.y = y
            pygame.draw.rect(surface,tile.color,tile.rect)
            y += 80
        
    def handleMouse(self,mousePos):
        if self.upRect.collidepoint(mousePos):
            if self.selectedItems[1] > 3:
                self.selectedItems[0] -= 1
                self.selectedItems[1] -= 1      
                self.activeTiles = self.tiles[self.selectedItems[0]:self.selectedItems[1]]
        if self.downRect.collidepoint(mousePos):
            if self.selectedItems[1] < len(self.tiles):
                self.selectedItems[0] += 1
                self.selectedItems[1] += 1
                self.activeTiles = self.tiles[self.selectedItems[0]:self.selectedItems[1]]
        for tile in self.activeTiles:
            if tile.rect.collidepoint(mousePos):
                self.activeTile = tile.char
        if not self.menuBackground.collidepoint(mousePos):
            print('outside menu')


    
        
        
    