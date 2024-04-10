import pygame

class Bullet:
    def __init__(self):
        self.image = pygame.image.load('bullet.png')
        self.x = 0
        self.y = 480
        self.x_change = 0
        self.y_change = 10
        self.state = "ready"

    def update(self, screen, player):
        if self.state == "fire":
            screen.blit(self.image, (self.x + 16, self.y + 10))
            self.y -= self.y_change
