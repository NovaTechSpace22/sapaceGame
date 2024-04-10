import pygame

class Explosion:
    def __init__(self, x, y):
        self.sprites = [pygame.image.load(f'explosion{n}.png') for n in range(1, 6)]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_speed = 0.5

    def update(self, screen):
        self.current_sprite += self.animation_speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0  # Reset or remove the explosion
        self.image = self.sprites[int(self.current_sprite)]
        screen.blit(self.image, self.rect)
