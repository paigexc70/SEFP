import pygame, sys
from pygame.locals import *
import random
import os
from settings import *

### Sprites ###
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()


all_sprites = pygame.sprite.Group()

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


    def draw(self):
        self.draw_grid()
        all_sprites.draw(self.DISPLAYSURF)
        pygame.display.flip()
            
    def draw_grid(self):
        for x in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            for y in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.DISPLAYSURF, WHITE, rect, 1)

    def update(self):
        all_sprites.update()

    def new(self):
        """
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add()
        self.run
        """   
        pass
      
    def quit(self):
        pygame.quit()
        sys.exit()
        
    def events(self):
        for event in pygame.event.get():
             if event.type == QUIT:
                 self.quit()

    

g = Game()
while True:
    g.run()
    


"""
if __name__ =="__main__":
    main()"""