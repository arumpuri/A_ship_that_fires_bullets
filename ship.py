import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """initialize the ship and set at initial position"""
        self.screen = ai_game.screen()
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and gets it rect
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()

        #start each new new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)