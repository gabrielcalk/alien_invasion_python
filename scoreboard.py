import pygame.font

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        # turn the numerical value stats.score into a string
        score_str = str(self.stats.score)
        #  pass this string to render(), which creates the image
        # To display the score clearly onscreen, we pass the screen’s background color and the text color to render()
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # We’ll position the score in the upper-right corner of the screen and
        # have it expand to the left as the score increases and the width of the number grows. To make sure the score always lines up with the right side of the
        # screen, we create a rect called score_rect w and set its right edge 20 pixels
        # from the right edge of the screen x. We then place the top edge 20 pixels
        # down from the top of the screen y
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)



