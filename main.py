import pygame, sys
from pygame.locals import *
import random
import os
from settings import *
from spritesheet import *

class Game:

    def __init__(self):
        pygame.init()  #initialize
        pygame.mixer.init()
        self.DISPLAYSURF = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run(self):
        #### run the game loop #####
        while True:

            for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #self.DISPLAYSURF.fill(GREY)
            pygame.display.flip()
            pygame.display.update()

    def draw(self):
        pass
            
    def draw_grid(self):
        pass

    def update(self):
        pass

    def events(self):
        pass

g = Game()
while True:
    g.run()
    g.new()


"""
if __name__ =="__main__":
    main()"""