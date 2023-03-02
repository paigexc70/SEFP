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
        self.DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZE),pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()
            self.draw_grid()
            self.new()
                        
            pygame.display.update()
            
    def quit(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.draw_grid()
        pygame.display.flip()
            
    def draw_grid(self):
        for x in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            for y in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.DISPLAYSURF, WHITE, rect, 1)

    def update(self):
        pass

    def new(self):
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