import pygame, sys
from pygame.locals import *
from settings import *
from main import *
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((WINDOW_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * WINDOW_SIZE
        self.rect.y = self.y * WINDOW_SIZE
        
"""