# libraries
import pygame

# components
from button import Button
from keyboard import Keyboard
from squares import Squares

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
squares = Squares(game_window)
# draw squares
squares.draw()

# initialize keyboard
keyboard = Keyboard(game_window)
# create keyboard buttons
keyboard.create()
# render keyboard
keyboard.render()

# app input
input = []

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
            elif command == 'Back':
                input.pop()
            else:
                input.append(command)

    pygame.display.update()

    fps.tick(screen_update)

pygame.quit()
