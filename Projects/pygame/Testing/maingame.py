import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2 - 200, screen.get_height() / 2)

fallingConst = 500
jumpSpeed = -550
vertSpeed = 0

pipe = pygame.Rect(500,200,100,200)
pipeSpeed = 90
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            vertSpeed = jumpSpeed
            print("move")
        if event.type == pygame.QUIT:
            running = False

    player_pos.y += vertSpeed * dt
    vertSpeed += fallingConst * dt

    pipe.x -= pipeSpeed * dt

    screen.fill("purple")
    pygame.draw.circle(screen,'red', player_pos, 50)
    pygame.draw.rect(screen, 'green', pipe,0)

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

