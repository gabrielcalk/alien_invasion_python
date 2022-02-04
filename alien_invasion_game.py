# We’ll use tools in the sys module to exit the game when the player quits.
import sys
# The pygame module contains the functionality we need to make a game
import pygame
# We import the sleep() function from the time module in the Python
# standard library so we can pause the game for a moment when the ship is hit
from time import sleep

# making an instance of Settings in the project and use it to access our settings
from settings.settings import Settings
from ship import Ship
from bullet import Bullet
from special_bullet import SpeacialBullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    def __init__(self):
        # the pygame.init() function initializes all imported pygame modules.
        pygame.init()

        # creating an instance of Settings and assign it to self.settings
        self.settings = Settings()

        # We call pygame.display.set_mode() to create a display window, on which we’ll draw all the game’s graphical elements
        # The argument (1200, 800) is a tuple that defines the dimensions of the game window, which will be 1200 pixels wide by 800 pixels high (from the settings atribute)
        # The object we assigned to self.screen is called a surface
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height)
        # )

        # When creating the screen surface, we pass a size of (0, 0) and the
        # parameter pygame.FULLSCREEN u. This tells Pygame to figure out a window size
        # that will fill the screen.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Because we don’t know the width and height of the
        # screen ahead of time, we update these settings after the screen is created
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # this function will change the name on the window.
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)

        # passing the game to the ship
        self.ship = Ship(self)

        # behaves like a list with some extra
        # functionality that’s helpful when building games. We’ll use this group
        # to draw bullets to the screen on each pass through the main loop and to
        # update each bullet’s position
        self.bullets = pygame.sprite.Group()
        self.special_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the Play button.
        self.play_button = Button(self, "Play")


    # The game is controlled by the run_game() method
    def run_game(self):
        # Start the main loop for the game
        while True:
            # Checking events
            self._check_events()

# In the main loop, we always need to call _check_events(), even if the
# game is inactive. For example, we still need to know if the user presses Q to
# quit the game or clicks the button to close the window. We also continue
# updating the screen so we can make changes to the screen while waiting to
# see whether the player chooses to start a new game. 

            if self.stats.game_active:
                self.ship.update()
                # Get rid of bullets that have disappeared and update each bullet on the screen (on the group)
                self._update_bullets()
                self._update_aliens()
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
            # Each keypress is registered as a KEYDOWN event
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_LCTRL:
            self._fire_bullet_special()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_bullets(self):
        # When you use a for loop with a list (or a group in Pygame), Python
        # expects that the list will staQy the same length as long as the loop is running. Because we can’t remove items from a list or group within a for loop,
        # we have to loop over a copy of the group
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        for special_bullet in self.special_bullets.copy():
            if special_bullet.rect.bottom <= 0:
                self.special_bullets.remove(special_bullet)

        # When you call update() on a group, the group automatically calls
        # update() for each sprite in the group. The line self.bullets.update() calls
        # bullet.update() for each bullet we place in the group bullets.
        self.bullets.update()
        self.special_bullets.update()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens.
        # The sprite.groupcollide() function compares the rects of each element
        # in one group with the rects of each element in another group. In this case,
        # it compares each bullet’s rect with each alien’s rect and returns a dictionary containing the bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        # The two True arguments tell Pygame to delete the bullets and aliens that have collided
        # (To make a high-powered bullet that can travel to the top of the screen, destroying every alien in its
        # path, you could set the first Boolean argument to False and keep the second
        # Boolean argument set to True.
        collisions = pygame.sprite.groupcollide(
            self.special_bullets, self.aliens, False, True)

        if not self.aliens:
            self._create_fleet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            # """Create a new bullet and add it to the bullets group."""
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _fire_bullet_special(self):
        if len(self.special_bullets) < self.settings.bullets_special_allowed:
            new_special_bullet = SpeacialBullet(self)
            self.special_bullets.add(new_special_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        # We need the width and height of an alien, so at u we use the attribute
        # size, which contains a tuple with the width and height of a rect object
        alien_width, alien_height = alien.rect.size
        # Spacing between each alien is equal to one alien width.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        #  Check if the fleet is at an edge,
        #  then update the positions of all aliens in the fleet.
        self._check_fleet_edges()
        self.aliens.update()
        # The spritecollideany() function takes two arguments: a sprite and a
        # group. The function looks for any member of the group that has collided
        # with the sprite and stops looping through the group as soon as it finds one
        # member that has collided with the sprite. Here, it loops through the group
        # aliens and returns the first alien it finds that has collided with ship
        # If no collisions occur, spritecollideany() returns None
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
             self._ship_hit()
        
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_screen(self):
        # We fill the screen with the background color using the fill() method, which acts on a surface and takes only one argument: a color.
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        for special_bullet in self.special_bullets.sprites():
            special_bullet.draw_bullet()

        # When you call draw() on a group, Pygame draws each element in the
        # group at the position defined by its rect attribute. The draw() method
        # requires one argument: a surface on which to draw the elements from the group
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()

        # The call to pygame.display.flip() tells Pygame to make the most recently drawn screen visible
        # When we move the game elements around, pygame.display.flip() continually updates the display to show the new positions of game elements and hides the old ones, creating the illusion of smooth movement.
        pygame.display.flip()
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 1:
            # Decrement ships_left .
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False


# We place run_game() in an if block that only runs if the file is called directly
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
