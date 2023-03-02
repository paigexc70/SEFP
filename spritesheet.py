import pygame, sys
from pygame.locals import *
from settings import *
from main import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30,40])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        




    def move(self):
        pass

    def update(self):
        pass
