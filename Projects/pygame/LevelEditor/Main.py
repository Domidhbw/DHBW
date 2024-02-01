import pygame
from listGenerator import LevelGenerator
from menu import selectMenu

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
running = True

level = LevelGenerator()
menu = selectMenu()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu.handleMouse(pygame.mouse.get_pos())
    
    level.update()

    screen.fill('black')

    level.drawLevel(screen)
    menu.drawMenu(screen)
    menu.drawTheTilesOnTheMenu(screen)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
