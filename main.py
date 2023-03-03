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
        
       # self.hitbox = (self.x, self.y, 0, 0)
        
        
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def get_random(self, x=0, y=0):
        self.x = random.randint(0, GRID_SIZE - 1)
        self.y = random.randint(0, GRID_SIZE - 1)
        
        
    
    def update(self):
        self.rect.x = self.x * CELL_SIZE
        self.rect.y = self.y * CELL_SIZE

    
# all_sprites = pygame.sprite.Group()
# hit_box = (x,x,x,x)

class Game:

    def __init__(self):
        pygame.init()  #initialize
        pygame.mixer.init()
        self.DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZE), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        pygame.mixer.music.load('music.wav')
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)

    def run_random(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS)
            self.random_events()
            self.draw()
            self.update()
           

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS)
            self.move_events()
            self.draw()
            self.update()
            pygame.display.update()
            pygame.mixer.music.load('music.wav')
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            
    def draw(self):
        self.DISPLAYSURF.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.DISPLAYSURF)

        #self.draw.rect(self.DISPLAYSURF, hit_box, player1, player2)

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

    def random_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                 self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.get_random()
                if event.key == pygame.K_RIGHT:
                    self.player2.get_random()

    def move_events(self):
        players_move_count = []
        player1_move_count = 0
        player2_move_count = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                 self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move(dx=-1)
                    player1_move_count += 1
                if event.key == pygame.K_RIGHT:
                    self.player.move(dx=1)
                    player1_move_count += 1
                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)
                    player1_move_count += 1
                if event.key == pygame.K_DOWN:
                    self.player.move(dy=1)
                    player1_move_count += 1
                if event.key == ord('a'):
                    self.player2.move(dx=-1)
                    player2_move_count += 1
                if event.key == ord('d'):
                    self.player2.move(dx=1)
                    player2_move_count += 1
                if event.key == ord('w'):
                    self.player2.move(dy=-1)
                    player2_move_count += 1
                if event.key == ord("s"):
                    self.player2.move(dy=1)        
                    player2_move_count += 1            
            
    def hit(self):
        print("Hooray! You've met in the woods")

    def checkCollisionx(self):
        pass

    def checkCollisionx(self):
        pass



g = Game()

grade_choice = ""

print("A. K - 2")
print("B. 3 - 5")
print("C. 6 - 8")
grade_choice = input("What grade level would you like to play: ")
grade_choice = grade_choice.lower()
if grade_choice == "a":
    while True:
        g.new()
        g.run_random()
        print()
if grade_choice == "b" or grade_choice == "c":
    while True:
        g.new()
        g.run()
        print()



    


"""
if __name__ =="__main__":
    main()"""