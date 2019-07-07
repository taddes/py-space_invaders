import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship to right
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip it onto the new screen."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
