# libraries
import pygame

# components
from button import Button
from keyboard import Keyboard
from input import Input

# set window dimensions
window_x = 265
window_y = 600

# set screen refresh rate
screen_update = 30

# set colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(108, 169, 101)
yellow = pygame.Color(200, 182, 83)
gray = pygame.Color(120, 124, 127)
lightgray = pygame.Color(230, 232, 234)

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

# word
word = "HELLO"
# current input
input_str = []

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
            if not command:
                pass
            elif command == 'Enter':
                print("Enter")
                pass
                # squares.enter(input)
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
                squares.check(word, ''.join(input_str))
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
