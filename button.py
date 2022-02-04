# First, we import the pygame.font module, which lets Pygame render text to the screen.
import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def draw_button(self):
        # Draw blank button and then draw message.
        # We call screen.fill() to draw the rectangular portion of the button.
        # Then we call screen.blit() to draw the text image to the screen, passing it
        # an image and the rect object associated with the image. This completes the
        # Button class.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    # Pygame works with text by rendering the string you want to display as an image.
    def _prep_msg(self, msg):
        # """Turn msg into a rendered image and center text on the button."""
        # The call to font.render() turns the text stored in msg into an image, which we then store in self.msg_image
        # The font.render() method also takes a Boolean value to turn antialiasing on or off (antialiasing makes the edges of the text smoother).
        # We set antialiasing to True and set the text background (by default is transparent) to the same color as the button.
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center






