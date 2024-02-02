# libraries
import pygame
import random
import time

# components
from keyboard import Keyboard
from input import Input

# additional files
from colors import colors

# set window dimensions
window_x = 265
window_y = 600

# initialize pygame
pygame.init()

# initialize pygame window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Wordle")

# refresh rate
fps = pygame.time.Clock()

# initialize input squares
squares = Input(game_window)
# create squares
squares.create()
# render squares
squares.render()

# initialize keyboard
keyboard = Keyboard(game_window)
# create keyboard buttons
keyboard.create()
# render keyboard
keyboard.render()

# for quick random search
words = []
# for quick checking of the dictionary
word_set = set()

lines = open('words.txt').read().splitlines()
for l in lines:
    word = l.upper()
    words.append(word)
    word_set.add(word)

# word
word = random.choice(words)
# current input
input_str = []

# track attempts
attempts = 0
# track the completion of the game
complete = False


def clear_message():
    surf = pygame.Surface((game_window.get_width(), 40), masks=(0, 0, 0))
    game_window.blit(surf, (0, 400))


def show_message(text):
    clear_message()
    font = pygame.font.SysFont('times new roman', 20)
    text_rendered = font.render(text, True, colors['white'])

    text_width = text_rendered.get_width()

    text_left = (game_window.get_width() - text_width) / 2
    text_top = 400

    game_window.blit(text_rendered, (text_left, text_top))


def handle_enter():
    valid = False
    input_word = ''.join(input_str).upper()
    if len(input_word) == 5:
        if input_word in word_set:
            valid = True
            # get letter colors
            correct, letter_themes = squares.check(word, ''.join(input_str))
            # apply colors to keyboard
            keyboard.apply_themes(letter_themes)
            input_str.clear()
            if correct:
                show_message('Great job!')
                return True, valid
        else:
            show_message('Word not in the list')
    else:
        show_message('Too short')

    return False, valid


def handle_backspace():
    clear_message()
    if len(input_str) > 0:
        input_str.pop()
        squares.back()


running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # handle mouse clicks on keyboard
            command = keyboard.find_button(pos)
            if not command:                     # click not on buttons
                pass
            elif command == 'Enter':            # mouse click on Enter
                complete, valid = handle_enter()
                if valid:
                    attempts += 1
            elif command == 'Back':
                handle_backspace()
            else:
                if len(input_str) < 5:
                    input_str.append(command)
                    squares.enter(command)
        if event.type == pygame.KEYDOWN and not complete:
            if event.key == pygame.K_RETURN:
                complete, valid = handle_enter()
                if valid:
                    attempts += 1
                if attempts == 6:
                    show_message("Word: " + word)
            if event.key == pygame.K_BACKSPACE:
                handle_backspace()
            if 97 <= event.key <= 122:
                if len(input_str) < 5:
                    input_str.append(event.unicode.upper())
                    squares.enter(event.unicode.upper())

    pygame.display.update()

pygame.quit()
