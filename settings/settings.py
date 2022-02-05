# Each time we introduce new functionality into the game, we’ll typically
# create some new settings as well. Instead of adding settings throughout
# the code, let’s write a module called settings that contains a class called
# Settings to store all these values in one place

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        # Pygame creates a black screen by default, but that’s boring. Let’s set a different background color
        # Colors in Pygame are specified as RGB colors: a mix of red, green, and blue
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Bullet Special settings
        self.bullet_special_speed = 10
        self.bullet_special_speed = 2
        self.bullet_special_width = 6
        self.bullet_special_height = 25
        self.bullet_special_color = (255, 0, 0)
        self.bullets_special_allowed = 1

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # 1 = right and -1 = left
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 5
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
