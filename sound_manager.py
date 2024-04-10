import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            "shoot": pygame.mixer.Sound('shoot.wav'),
            "explosion": pygame.mixer.Sound('explosion.wav'),
            "powerup": pygame.mixer.Sound('powerup.wav'),
        }

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()
