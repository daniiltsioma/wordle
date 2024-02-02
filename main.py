# libraries
import pygame
import random

# components
from keyboard import Keyboard
from input import Input

# set window dimensions
window_x = 265
window_y = 600

# set screen refresh rate
screen_update = 30

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
print(word)

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
                print('enter click')
                input_word = ''.join(input_str)
                if len(input_word) == 5:
                    if input_word in word_set:
                        print(word, 'in word set')
                        # get letter colors
                        letter_themes = squares.check(word, ''.join(input_str))
                        # apply colors to keyboard
                        keyboard.apply_themes(letter_themes)
                        input_str.clear()
                    else:
                        print("Word not in the list")
                else:
                    print("Too short")
            elif command == 'Back':
                if len(input_str) > 0:
                    input_str.pop()
                    squares.back()
            else:
                if len(input_str) < 5:
                    input_str.append(command)
                    squares.enter(command)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(input_str) == 5:
                    letter_themes = squares.check(word, ''.join(input_str))
                    keyboard.apply_themes(letter_themes)
                    input_str.clear()
            if event.key == pygame.K_BACKSPACE:
                if len(input_str) > 0:
                    input_str.pop()
                    squares.back()
            if 97 <= event.key <= 122:
                if len(input_str) < 5:
                    input_str.append(event.unicode.upper())
                    squares.enter(event.unicode.upper())

    pygame.display.update()

    fps.tick(screen_update)

pygame.quit()
