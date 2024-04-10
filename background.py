import pygame

class Background:
    def __init__(self):
        self.background_image = pygame.image.load('background.png')

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
