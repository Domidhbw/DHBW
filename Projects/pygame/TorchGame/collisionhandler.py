import pygame

class collisionHandler:
    def __init__(self) -> None:
        pass

    def update(self,player,collisionmap):
        player.updatePosition()

        for item in collisionmap:
            if item.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = item.rect.right
                elif player.direction.x > 0:
                    #from right
                    player.rect.right = item.rect.left
        for item in collisionmap:
            if item.rect.colliderect(player.rect):              
                if player.direction.y > 0:
                    player.rect.bottom = item.rect.top
                elif player.direction.y < 0:
                    player.rect.top = item.rect.bottom


    
