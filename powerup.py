import pygame
import random

class PowerUp:
    def __init__(self):
        self.image = pygame.image.load('powerup.png')
        self.x = random.randint(0, 736)
        self.y = 0
        self.y_change = 5

    def update(self, screen):
        self.y += self.y_change
        if self.y > 600:
            self.x = random.randint(0, 736)
            self.y = 0
        screen.blit(self.image, (self.x, self.y))
