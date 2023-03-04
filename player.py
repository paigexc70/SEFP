### Sprites ###

import pygame, sys
from pygame.locals import *
import random
import os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface([CELL_SIZE, CELL_SIZE])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y        
        
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def get_random(self, x=0, y=0):
        self.x = random.randint(0, GRID_SIZE_LENGHT - 1)
        self.y = random.randint(0, GRID_SIZE_HEIGHT - 1)
        
        
    def update(self):
        self.rect.x = self.x * CELL_SIZE
        self.rect.y = self.y * CELL_SIZE
        
    def remove(self):
        self.kill()
   
        