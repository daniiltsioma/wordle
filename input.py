import pygame

from square import Square

gray = pygame.Color(120, 124, 127)


class Input:
    def __init__(self, window):
        self.window = window
        self.squares = []
        self.current = 0  # current index

    def create(self):
        offset_top = 20
        for i in range(6):
            offset_left = 10
            for j in range(5):
                self.squares.append(
                    Square(self.window, offset_left, offset_top, 41, 41, gray))
                offset_left += 51
            offset_top += 51

    def render(self):
        for sq in self.squares:
            sq.render()

    def enter(self, key):
        self.squares[self.current].input(key)
        self.current += 1

    def back(self):
        self.current -= 1
        self.squares[self.current].clear()
