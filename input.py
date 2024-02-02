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
                    Square(self.window, offset_left, offset_top, 41, 41, 0))
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

    def check(self, word, user_input):
        letter_dict = dict()
        letter_themes = dict()
        for l in word:
            if l in letter_dict:
                letter_dict[l] += 1
            else:
                letter_dict[l] = 1
        start = self.current - 5
        letter_apps = dict()
        for i in range(5):
            if user_input[i] == word[i]:
                self.squares[start + i].set_theme(1)
                letter_themes[user_input[i]] = 1
            elif user_input[i] in letter_dict and user_input[i] in letter_apps and letter_apps[user_input[i]] < letter_dict[user_input[i]]:
                self.squares[start + i].set_theme(2)
                letter_themes[user_input[i]] = 2
            else:
                self.squares[start + i].set_theme(3)
                letter_themes[user_input[i]] = 3
        return letter_themes
