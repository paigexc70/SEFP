import pygame, sys
from pygame.locals import *
from settings import *
from main import *

class Player(pygame.sprite.Sprite):
    def __init__(self, WINDOW_SIZE, pos_x, pos_y,):
        super().__init__()
        self.image = pygame.Surface([WINDOW_SIZE])
        self.image.fill(255, 255, 0)
        self.rect = self.image.get_rect()
        



    """
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * WINDOW_SIZE
        self.rect.y = self.y * WINDOW_SIZE
    """   
