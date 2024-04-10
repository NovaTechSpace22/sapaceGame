import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('enemy.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = 4
        self.y_change = 40

    def update(self, screen):
        self.x += self.x_change
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change
        screen.blit(self.image, (self.x, self.y))
