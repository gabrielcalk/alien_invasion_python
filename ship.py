import pygame

# from alien_invasion_game import AlienInvasion

# This class will manage most of the behavior of the player’s ship:

class Ship:
    # The __init__() method of Ship takes two parameters: the self reference and a reference to
    # the current instance of the AlienInvasion class. This will give Ship access to
    # all the game resources defined in AlienInvasion
    def __init__(self, ai_game):
        # we assign the screen to an attribute of Ship, so we can access it easily in all the methods in this class
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Pygame is efficient because it lets you treat all game elements like rectangles (rects), even if they’re not exactly shaped like rectangles. Treating
        # an element as a rectangle is efficient because rectangles are simple geometric shapes
        # we access the screen’s rect attribute using the get_rect() method and assign it to self.screen_rect.
        # Doing so allows us to place the ship in the correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # To load the image, we call pygame.image.load()
        self.image = pygame.image.load('images/ship.bmp')

        # When the image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later use it to place the ship
        self.rect = self.image.get_rect()

        # position the ship at the bottom center of the screen (adding to the rect object that will contains now the position that the image will be and the image size).
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_down = False

    def update(self):
        #  """Update the ship's position based on the movement flag."""
        # 2 if with no else if because if the user click on right and left the ship will stay on the same spot
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >= 0:
            self.x -= self.settings.ship_speed
        if self.moving_top and self.rect.top > 900:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


#  You can use a decimal value to set an attribute of rect, but the rect will only
# keep the integer portion of that value.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


# About the rect object

# When you’re working with a rect object, you can use the x- and y-coordinates of the top, bottom, left, and right edges of the rectangle, as well as the
# center, to place the object. You can set any of these values to establish the current position of the rect

# In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
# increase as you go down and to the right. On a 1200 by 800 screen, the origin is
# at the top-left corner, and the bottom-right corner has the coordinates (1200, 800).
# These coordinates refer to the game window, not the physical screen.

# When you’re centering a game element, work
# with the center, centerx, or centery attributes of a rect. When you’re working
# at an edge of the screen, work with the top, bottom, left, or right attributes.
# There are also attributes that combine these properties, such as midbottom,
# midtop, midleft, and midright. When you’re adjusting the horizontal or vertical placement of the rect, you can just use the x and y attributes, which are
# the x- and y-coordinates of its top-left corner.
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)