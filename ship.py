import pygame

class Ship():
    """Class for behavior of the ship."""
    
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start new ship at bottom center of screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)