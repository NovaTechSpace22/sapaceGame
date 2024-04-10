import pygame

class Scoreboard:
    def __init__(self, x, y):
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y

    def draw(self, screen):
        score_display = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_display, (self.x, self.y))

    def increase_score(self, amount):
        self.score += amount
