
import pygame

# set window dimensions
window_x = 480
window_y = 720

# set colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(108, 169, 101)
yellow = pygame.Color(200, 182, 83)
gray = pygame.Color(120, 124, 127)

# initialize pygame
pygame.init()

# initialize pygame window
pygame.display.set_caption("Wordle")
game_window = pygame.display.set_mode((window_x, window_y))