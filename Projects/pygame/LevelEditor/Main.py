import pygame
from listGenerator import LevelGenerator
from menu import selectMenu


pygame.init()
screen = pygame.display.set_mode((1800,900))
clock = pygame.time.Clock()
running = True

level = LevelGenerator()
level.createLevel()
menu = selectMenu()
reloadLevel = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.handleMouse(pygame.mouse.get_pos(),level.currentShift):
                reloadLevel = True
    
    level.update()

    screen.fill('black')

    level.drawLevel(screen)
    menu.drawMenu(screen)
    menu.drawTheTilesOnTheMenu(screen)

    if reloadLevel:
        level.createLevel()
        reloadLevel = False

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
