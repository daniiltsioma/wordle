# libraries
import pygame

# additional files
from colors import colors


class Square:
    themes = [
        (0, colors['gray'], colors['white']),                  # default
        (1, colors['green'], colors['white']),                 # green
        (2, colors['yellow'], colors['white']),                # yellow
        (3, colors['gray'], colors['white']),                  # gray
    ]

    def __init__(self, window, x, y, width, height, theme):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.theme = self.themes[theme]
        self.textColor = pygame.Color(255, 255, 255)
        self.font = pygame.font.SysFont('times new roman', 25)
        self.rect = None
        self.text = ''

    def input(self, char):
        self.text = char
        self.render_text()

    def clear(self):
        surf = pygame.Surface((39, 39))
        self.window.blit(surf, (self.x + 1, self.y + 1))
        self.text = ''

    def set_theme(self, index):
        self.theme = self.themes[index]
        self.render()

    def render_text(self):
        # render text in this font
        self.text_rendered = self.font.render(self.text, True, self.textColor)

        text_width = self.text_rendered.get_width()
        text_height = self.text_rendered.get_height()

        text_left = self.x + (self.width - text_width) / 2
        text_top = self.y + (self.height - text_height) / 2

        self.window.blit(self.text_rendered, (text_left, text_top))

    def render(self):
        fill = self.theme[0] < 1
        self.rect = pygame.draw.rect(self.window, self.theme[1],
                                     (self.x, self.y, self.width, self.height), fill)
        self.render_text()
