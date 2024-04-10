import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('player.png')
        self.x = x
        self.y = y
        self.x_change = 0

    def update(self, screen):
        self.x += self.x_change
        screen.blit(self.image, (self.x, self.y))

    # Add movement methods here
