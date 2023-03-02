import pygame, sys
from pygame.locals import *

######### global variables ########
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (50, 50, 50)
clock = pygame.time.Clock()
FPS = 60
GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
pygame.display.set_caption('Project')


