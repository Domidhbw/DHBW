import pygame
from testLevel import *
from TileManager import TileManager
import math

class selectMenu:
    def __init__(self) -> None:
        self.selectedItems = [0,3]
        self.tiles = list()
        self.upRect = pygame.rect.Rect(1720,50,60,50)
        self.upButton = [[1720,100],[1750,50],[1780,100]]
        self.downRect = pygame.rect.Rect(1720,500,60,50)
        self.downButton = [[1720,500],[1750,550],[1780,500]]
        self.activeTile = 'x'
        self.tileManager = TileManager()
        self.createTilesAndAssignThemToList()
        self.activeTiles = self.tiles[self.selectedItems[0]:self.selectedItems[1]]
        self.menuBackground = pygame.rect.Rect((1700,0,100,600))
        self.saveButton = pygame.rect.Rect(1720,5,50,20)            

    def drawMenu(self,screen):
        pygame.draw.rect(screen,'red',self.menuBackground)
        pygame.draw.polygon(screen, (0, 255, 255), self.upButton)
        pygame.draw.polygon(screen, (0, 255, 255), self.downButton)
        pygame.draw.rect(screen,'blue',self.saveButton)

    def createTilesAndAssignThemToList(self):
        chars = list(tiles.keys())
        for char in chars:
            self.tiles.append(self.tileManager.createTile(char,0,0))
        
    def drawTheTilesOnTheMenu(self,surface):
        x = 1710
        y = 200
        for tile in self.activeTiles:
            tile.rect.x = x
            tile.rect.y = y
            surface.blit(tile.sprite,(tile.rect.x,tile.rect.y))
            y += 80
        
    def handleMouse(self,mousePos,shift):
        if self.saveButton.collidepoint(mousePos):
            self.saveToFile()
            pass
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
        shift.x = -shift.x
        posToPlaceCharAt = self.calculateXandYtoPlace(mousePos)
        self.placeTileConsideringShift(posToPlaceCharAt,shift)
    

    def placeTileConsideringShift(self, screen_position, currentShift):
        # Convert screen position to world coordinates by adding the shift

        world_position_x = screen_position.x -1 
        world_position_y = screen_position.y -1 

        # Ensure world positions are within level bounds
        world_position_x = int(max(0, min(world_position_x, len(level_map[0]) - 1)))
        world_position_y = int(max(0, min(world_position_y, len(level_map) - 1)))

        # Find and update the specific cell in world coordinates
        if 0 <= world_position_y < len(level_map) and 0 <= world_position_x < len(level_map[0]):
            row = level_map[world_position_y]
            updated_row = row[:world_position_x] + self.activeTile + row[world_position_x + 1:]
            level_map[world_position_y] = updated_row
        else:
            print(f"Position out of bounds: {world_position_x}, {world_position_y}")



    def calculateXandYtoPlace(self,mousePos):
        return pygame.Vector2(math.ceil(mousePos[0]/64),math.ceil(mousePos[1]/64))


    def saveToFile(self):
        f = open('level.txt','w')
        for item in level_map:
            print(item)
            moditem = item.replace('o',' ')
            f.write('\''+ moditem+'\'' + ',' +'\n')
       
        pass
        
        
    