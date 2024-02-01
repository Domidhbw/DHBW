import pygame
import random

ENEMY_SPEED = 3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Enemy class
class Enemy():
    def __init__(self, player_rect):
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 55), random.randint(0, SCREEN_HEIGHT - 55), 55, 55)
        self.player_rect = player_rect
        self.color = 'red'
        self.alive = True

    def chasePlayer(self):
        player_x, player_y = self.player_rect.center
        enemy_x, enemy_y = self.rect.center

        if abs(player_x - enemy_x) > abs(player_y - enemy_y):
            if player_x < enemy_x:
                self.rect.x -= ENEMY_SPEED
            elif player_x > enemy_x:
                self.rect.x += ENEMY_SPEED
        else:
            if player_y < enemy_y:
                self.rect.y -= ENEMY_SPEED
            elif player_y > enemy_y:
                self.rect.y += ENEMY_SPEED

    def checkForCollision(self,killer):
        if self.rect.colliderect(killer):
            self.die()
        else:
            self

    def die(self):
        self.color = 'black'

    def update(self,killer):
        self.chasePlayer()
        self.checkForCollision(killer)