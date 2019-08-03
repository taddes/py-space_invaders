import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init___()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load alien image and set rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

    def bltime(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)