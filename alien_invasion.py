import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create ship
    ship = Ship(ai_settings, screen)
    #  Make a group to store bullets
    bullets = Group()
    
    screen.fill(ai_settings.bg_color)

    """Initialte game loop"""
    while True:
        # Watch for keyboard or mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

        
        

run_game()
