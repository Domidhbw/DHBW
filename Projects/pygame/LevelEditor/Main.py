import pygame
from tile import Tile

pygame.init()
screen = pygame.display.set_mode((500, 250))
clock = pygame.time.Clock()
running = True

xForTile = 0
yForTile = 0

level = open("testLevel.txt","r").read()
listOfTiles = list()

for char in level:
    match char:
        case "x":
            listOfTiles.append(Tile(xForTile,yForTile,"Blue"))
            xForTile += 50
        case "o":
            listOfTiles.append(Tile(xForTile,yForTile,"Black"))
            xForTile += 50
        case ",":
            xForTile = 0
            yForTile += 50


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for tile in listOfTiles:
        tile.draw(screen)
    # RENDER YOUR GAME HERE

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
