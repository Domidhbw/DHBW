import pygame
from tile import Tile
from testLevel import *

class TileManager:
    def __init__(self) -> None:
        self.tileInformation = tiles

    def createTile(self,char,left,top):
        if char in self.tileInformation.keys():
            return Tile(left,top,self.tileInformation[char],char)
        else:
            print('key does not exist check your colors and test level')

    

