# We’ll use tools in the sys module to exit the game when the player quits.
import sys
# The pygame module contains the functionality we need to make a game
import pygame

# making an instance of Settings in the project and use it to access our settings
from settings.settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        # the pygame.init() function initializes all imported pygame modules.
        pygame.init()

        # creating an instance of Settings and assign it to self.settings
        self.settings = Settings()

        # We call pygame.display.set_mode() to create a display window, on which we’ll draw all the game’s graphical elements
        # The argument (1200, 800) is a tuple that defines the dimensions of the game window, which will be 1200 pixels wide by 800 pixels high (from the settings atribute)
        # The object we assigned to self.screen is called a surface
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # this function will change the name on the window.
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    # The game is controlled by the run_game() method
    def run_game(self):
        # Start the main loop for the game
        while True:
            # Checking events
            self._check_events()
            # updating the screen
            self._update_screen()


    # A helper methods does work inside a class but isn’t meant to be called through an instance.
    # In Python, a single leading underscore indicates a helper method
    def _check_events(self):
        # An event is an action that the user performs while playing the game, such as pressing a key or moving the mouse.
        # To access the events that Pygame detects, we’ll use the pygame.event.get() function
        # This function returns a list of events that have taken place since the last time this function was called.
        # Any keyboard or mouse event will cause this for loop to run.
        for event in pygame.event.get():
            # when the player clicks the game window’s close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # We fill the screen with the background color using the fill() method, which acts on a surface and takes only one argument: a color.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        # The call to pygame.display.flip() tells Pygame to make the most recently drawn screen visible
        # When we move the game elements around, pygame.display.flip() continually updates the display to show the new positions of game elements and hides the old ones, creating the illusion of smooth movement.
        pygame.display.flip()


# We place run_game() in an if block that only runs if the file is called directly
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
