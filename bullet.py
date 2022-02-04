import pygame
from pygame.sprite import Sprite

# When you use sprites, you can group related elements in
# your game and act on all the grouped elements at once. 
class Bullet(Sprite):
    #  """Create a bullet object at the ship's current position."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

         # Create a bullet rect at (0, 0) and then set correct position.
        # The bullet isn’t based on an image, so we have to build a rect from scratch using the pygame.Rect() class. 
        # This class requires the x- and y-coordinates of the top-left corner of the rect, and the width and height of the rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # we set the bullet’s midtop attribute to match the ship’s midtop attribute. This will make the bullet emerge from the top of the ship, making it
        # look like the bullet is fired from the ship.
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        # """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        #  """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
