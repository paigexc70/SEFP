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
        self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run(self):
        #### run the game loop #####
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS) / 1000
            self.events()
            self.update()
            self.draw()

            
            pygame.display.update()
            
    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.draw_grid()
        pygame.display.flip()
            
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.DISPLAYSURF, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.DISPLAYSURF, LIGHTGREY, (0, y), (WIDTH, y))

    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
             if event.type == QUIT:
                 self.quit()

    

g = Game()
while True:
    g.run()
    g.new()


"""
if __name__ =="__main__":
    main()"""