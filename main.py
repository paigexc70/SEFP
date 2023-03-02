import pygame, sys
from pygame.locals import *
import random
import os
from settings import *

### Sprites ###
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

    def update(self):
        self.rect.x = self.x * CELL_SIZE
        self.rect.y = self.y * CELL_SIZE


# all_sprites = pygame.sprite.Group()

class Game:

    def __init__(self):
        pygame.init()  #initialize
        pygame.mixer.init()
        self.DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZE), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS)
            self.events()
            self.draw()
            self.update()
            #self.new()
            pygame.display.update()
            pygame.mixer.music.load('music.wav')
            pygame.mixer.music.play(-1)
            
    def draw(self):
        self.DISPLAYSURF.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.DISPLAYSURF)
        pygame.display.flip()     
        
    def draw_grid(self):
        for x in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            for y in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.DISPLAYSURF, WHITE, rect, 1)   
                
    def update(self):
        self.all_sprites.update()         
            
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, 0,0)
        self.player2 = Player(self, 9,9)
        self.all_sprites.add(self.player, self.player2)         
        
             
    def quit(self):
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                 self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(dy=1)
                if event.key == ord('a'):
                    self.player2.move(dx=-1)
                if event.key == ord('d'):
                    self.player2.move(dx=1)
                if event.key == ord('w'):
                    self.player2.move(dy=-1)
                if event.key == ord("s"):
                    self.player2.move(dy=1)                    


g = Game()

while True:
    g.new()
    g.run()
    


"""
if __name__ =="__main__":
    main()"""