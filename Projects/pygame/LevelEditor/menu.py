import pygame
from testLevel import *
from TileManager import TileManager
import math

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
        
    def handleMouse(self,mousePos,shift):
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
            self.placeTile(mousePos,shift)
            return True

    def placeTile(self,mousePos,shift):
        posToPlaceCharAt = self.calculateXandYtoPlace(mousePos)
        posToPlaceCharAt += self.roundTheShift(shift)
        print(self.roundTheShift(shift))
        self.placeTileInFile(posToPlaceCharAt)
    
    def roundTheShift(self,shift):
        print('shift' + str(shift))
        return pygame.Vector2(math.ceil(shift.x/2205),math.ceil(shift.y/2205))

    def placeTileInFile(self,position):
        print(position)
        for rowIndex, row in enumerate(level_map):
            if rowIndex == position.y -1:
                for colIndex, cell in enumerate(row):
                    if colIndex == position.x -1:
                        # Reconstruct the string with the replacement
                        updated_row = row[:colIndex] + self.activeTile + row[colIndex + 1:]
                        # Update the row in level_map
                        level_map[rowIndex] = updated_row


                        

    def calculateXandYtoPlace(self,mousePos):
        return pygame.Vector2(math.ceil(mousePos[0]/64),math.ceil(mousePos[1]/64))


    
        
        
    