import pygame
import sys
from wall import Wall
from player import Player
pygame.init()

#Constants
WIDTH, HEIGHT = 800,600
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    player.update()

    for wall in walls:
        if player.rect.colliderect(wall):
            player.wallHit()

    # Draw everything on the screen
    screen.fill((0, 0, 0))  

    pygame.draw.rect(screen,'green',player.rect)

    for wall in walls:
        pygame.draw.rect(screen,'blue',wall.rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()