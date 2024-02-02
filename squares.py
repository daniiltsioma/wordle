import pygame

gray = pygame.Color(120, 124, 127)


class Squares:
    def __init__(self, window):
        self.window = window
        self.squares = []

    def draw(self):
        offset_top = 20
        for i in range(6):
            offset_left = 10
            for j in range(5):
                self.squares.append(pygame.draw.rect(self.window, gray,
                                                     (offset_left, offset_top, 41, 41), 1))
                offset_left += 51
            offset_top += 51
