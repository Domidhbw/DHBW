import pygame
import sys
from wall import Wall
from player import Player
from collisionhandler import collisionHandler
from enemy import Enemy
pygame.init()

#Constants
WIDTH, HEIGHT = 1200,900
FPS = 60

#Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flash Light')
clock = pygame.time.Clock()
running = True

#initialize objects
player = Player()
topWall = Wall(0,0,WIDTH,20)
bottomWall = Wall(0,HEIGHT-20,WIDTH,20)
leftWall = Wall(0,0,20,HEIGHT)
rightWall = Wall(WIDTH-20,0,20,HEIGHT)
walls = [topWall, bottomWall, leftWall, rightWall]
ememy = Enemy(player.rect)

collisionHandler = collisionHandler()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    target_x, target_y = pygame.mouse.get_pos()
                    player.shoot(target_x, target_y)

    # Update game objects
    player.getInput()
    collisionHandler.update(player,walls)
    ememy.chasePlayer()
    # Draw everything on the screen
    screen.fill((0, 0, 0))  
    for bullet in player.bullets:
        bullet.updatePosition()
        
    pygame.draw.rect(screen,'green',player.rect)
    pygame.draw.rect(screen,'green',ememy.rect)
    for wall in walls:
        pygame.draw.rect(screen,'blue',wall.rect)
    for bullet in player.bullets:
         pygame.draw.rect(screen, 'red', bullet.rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()