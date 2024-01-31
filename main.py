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

# button font
smallfont = pygame.font.SysFont('times new roman', 20)


# initialize pygame window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Wordle")

# refresh rate
fps = pygame.time.Clock()

letters = 'qwertyuiop'
buttons: list[Button] = []

offset_left = 10
for ltr in letters:
    buttons.append(Button(game_window, ltr, 0, offset_left,
                   200, 20, 30, smallfont))
    offset_left += 25

letters = 'asdfghjkl'
offset_left = 25
for ltr in letters:
    buttons.append(Button(game_window, ltr, 0, offset_left,
                   235, 20, 30, smallfont))
    offset_left += 25

letters = 'zxcvbnm'
offset_left = 50
for ltr in letters:
    buttons.append(Button(game_window, ltr, 0, offset_left,
                   270, 20, 30, smallfont))
    offset_left += 25

running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # q_button.render(game_window)
    for btn in buttons:
        btn.render(game_window)

    mouse = pygame.mouse.get_pos()

    pygame.display.update()

    fps.tick(screen_update)

pygame.quit()
