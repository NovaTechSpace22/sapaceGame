import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
from background import Background

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = Background()

# Player
player = Player(screen_width / 2, screen_height - 100)

# Enemy
enemies = [Enemy() for _ in range(5)]

# Bullet
bullet = Bullet()

# Game Loop
def run_game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        background.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(screen)
        for enemy in enemies:
            enemy.update(screen)
        bullet.update(screen, player)

        pygame.display.update()

if __name__ == "__main__":
    run_game()
