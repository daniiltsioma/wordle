import pygame


class Square:
    def __init__(self, window, x, y, width, height, color):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.input = ''

    def input(self, char):
        self.input = char

    def clear(self):
        self.input = ''

    def render(self):
        pygame.draw.rect(self.window, self.color,
                         (self.x, self.y, self.width, self.height), 1)
