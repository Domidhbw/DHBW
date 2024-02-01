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
direction = -20
onOrOff = True

collisionHandler = collisionHandler()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if onOrOff:
            onOrOff = False
        else:
            onOrOff = True

    # Update game objects
    player.getInput()
    collisionHandler.update(player,walls)
    ememy.chasePlayer()
    # Draw everything on the screen
    screen.fill((0, 0, 0))  


    if player.direction.x > 0:
        direction = 80
    elif player.direction.x < 0:
        direction = -20

    pygame.draw.rect(screen,ememy.color,ememy.rect)
    pygame.draw.rect(screen,'green',player.rect)
    if onOrOff:
        pygame.draw.polygon(screen, (0, 255, 255), ((player.rect.center),(player.rect.x + direction,player.rect.y - 60),(player.rect.x + direction,player.rect.y + 115)))
    for wall in walls:
        pygame.draw.rect(screen,'blue',wall.rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()