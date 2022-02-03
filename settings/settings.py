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