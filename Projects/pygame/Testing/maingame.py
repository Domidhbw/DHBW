import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 45
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BIRD_SIZE = 40
GRAVITY = 0.9
JUMP_HEIGHT = 14  
PIPE_WIDTH = 50
PIPE_HEIGHT = 300
PIPE_GAP = 150

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    surface = font.render(text, True, WHITE)
    screen.blit(surface, (x, y))

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = -JUMP_HEIGHT

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)

    def update(self):
        self.x -= 5

# Create bird and pipes
bird = Bird()
pipes = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update
    bird.update()

    # Check for collisions
    if bird.y < 0 or bird.y + BIRD_SIZE > HEIGHT:
        pygame.quit()
        sys.exit()

    # Generate pipes
    if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
        pipe = Pipe(WIDTH)
        pipes.append(pipe)

    # Update pipes
    for pipe in pipes:
        pipe.update()

        # Check for collisions with pipes
        if (
            bird.x < pipe.x + PIPE_WIDTH
            and bird.x + BIRD_SIZE > pipe.x
            and (bird.y < pipe.height or bird.y + BIRD_SIZE > pipe.height + PIPE_GAP)
        ):
            pygame.quit()
            sys.exit()

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x + PIPE_WIDTH > 0]

    # Draw
    screen.fill(BLACK)

    # Draw bird
    pygame.draw.rect(screen, WHITE, (bird.x, bird.y, BIRD_SIZE, BIRD_SIZE))

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, WHITE, (pipe.x, 0, PIPE_WIDTH, pipe.height))
        pygame.draw.rect(screen, WHITE, (pipe.x, pipe.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe.height - PIPE_GAP))

    # Draw score
    draw_text("Score: {}".format(len(pipes) - 1), 10, 10)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
