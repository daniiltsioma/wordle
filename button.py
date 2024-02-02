# libraries
import pygame

# additional files
from colors import colors


class Button():

    themes = [
        (colors['lightgray'], colors['black']),             # default
        (colors['green'], colors['white']),                 # green
        (colors['yellow'], colors['white']),                # yellow
        (colors['gray'], colors['white']),                  # gray
    ]

    def __init__(self, window, text, theme, x, y, width, height, font_size):
        self.text = text
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.theme = self.themes[theme]
        self.font = pygame.font.SysFont('times new roman', font_size)
        self.rect = None

    def render(self):
        self.rect = pygame.draw.rect(self.window, self.theme[0], [
            self.x, self.y, self.width, self.height])

        self.render_text()

    def render_text(self):
        # render text in this font
        text = self.font.render(self.text, True, self.theme[1])

        text_width = text.get_width()
        text_height = text.get_height()

        text_left = self.x + (self.width - text_width) / 2
        text_top = self.y + (self.height - text_height) / 2

        self.window.blit(text, (text_left, text_top))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            return self.text

    def is_letter(self):
        return self.text != 'Enter' and self.text != 'Back'

    def set_theme(self, index):
        self.theme = self.themes[index]
        self.render()

    def get_text(self):
        return self.text
