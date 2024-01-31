# libraries
import pygame

# components
from button import Button

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


buttons: list[Button] = []

# keyboard top row
letters = 'qwertyuiop'
offset_left = 10
offset_top = window_y - 50 - (10 * 2) - (30 * 3)
for ltr in letters:
    buttons.append(Button(game_window, ltr, 0, offset_left,
                   offset_top, 20, 30, 20))
    offset_left += 25

# keyboard mid row
letters = 'asdfghjkl'
offset_left = 25
offset_top += 40
for ltr in letters:
    buttons.append(Button(game_window, ltr, 0, offset_left,
                   offset_top, 20, 30, 20))
    offset_left += 25

# keyboard bottom row
offset_left = 15
offset_top += 40
enter_button = Button(game_window, 'Enter', 0,
                      offset_left, offset_top, 30, 30, 10)
offset_left += 35

letters = 'zxcvbnm'
for ltr in letters:
    buttons.append(Button(game_window, ltr, 0, offset_left,
                   offset_top, 20, 30, 20))
    offset_left += 25

back_button = Button(game_window, 'Back', 0,
                     offset_left, offset_top, 30, 30, 10)

squares = []

offset_top = 20
for i in range(6):
    offset_left = 10
    for j in range(5):
        squares.append(pygame.draw.rect(game_window, gray,
                                        (offset_left, offset_top, 41, 41), 1))
        offset_left += 51
    offset_top += 51

running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # q_button.render(game_window)
    for btn in buttons:
        btn.render(game_window)
    enter_button.render(game_window)
    back_button.render(game_window)

    mouse = pygame.mouse.get_pos()

    pygame.display.update()

    fps.tick(screen_update)

pygame.quit()
