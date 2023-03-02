import pygame, sys
from pygame.locals import *
import random
import os
from settings import *
from spritesheet import *


"""
##### grid ###
for i in range(0, 500, 50):
    pygame.draw.line(DISPLAYSURF, (255, 255, 255), (0, i), (500, i))
    pygame.draw.line(DISPLAYSURF, (255, 255, 255),(i, 0), (i, 500))
"""

class Game:

    def __init__(self):
        pygame.init()  #initialize
        pygame.mixer.init()
        


    def run(self):
        #### run the game loop #####
        while True:

            clock.tick(FPS)

            for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                sys.exit()

            DISPLAYSURF.fill(GREY)
            pygame.display.flip()
            pygame.display.update()

    def draw(self):
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