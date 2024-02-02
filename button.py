# libraries
import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(108, 169, 101)
yellow = pygame.Color(200, 182, 83)
gray = pygame.Color(120, 124, 127)
lightgray = pygame.Color(230, 232, 234)


class Button():

    themes = [
        (lightgray, black),             # default
        (green, white),                 # green
        (yellow, white),                # yellow
        (gray, white),                  # gray
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
