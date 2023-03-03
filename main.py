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

    def collide(self, spriteGroup):
        pass
        #pygame.sprite.spritecollide(self, spriteGroup, False)

    
# all_sprites = pygame.sprite.Group()
# hit_box = (#,#,#,#)

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
           

    def run(self, player_count):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS)
            self.move_events(player_count)
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
            
    def new(self, player_count, grade_choice):
        self.all_sprites = pygame.sprite.Group()
        if grade_choice == "a":
            self.player1 = Player(self, 0, 0)
            self.player2 = Player(self, 9, 9)
            self.all_sprites.add(self.player1, self.player2) 
        if grade_choice == "b" or grade_choice == "c":
            if player_count == 3:
                player1_x = int(input("Player 1, please enter the x axis you want to start on: "))
                player1_y = int(input("Player 1, please enter the y axis you want to start on: "))
                self.player1 = Player(self, player1_x, player1_y)
                player2_x = int(input("Player 2, please enter the x axis you want to start on: "))
                player2_y = int(input("Player 2, please enter the y axis you want to start on: "))
                self.player2 = Player(self, player2_x, player2_y)
                player3_x = int(input("Player 3, please enter the x axis you want to start on: "))
                player3_y = int(input("Player 3, please enter the y axis you want to start on: "))
                self.player3 = Player(self, player3_x, player3_y)
                self.all_sprites.add(self.player1, self.player2, self.player3) 
            elif player_count == 4:
                player1_x = int(input("Player 1, please enter the x axis you want to start on: "))
                player1_y = int(input("Player 1, please enter the y axis you want to start on: "))
                self.player1 = Player(self, player1_x, player1_y)
                player2_x = int(input("Player 2, please enter the x axis you want to start on: "))
                player2_y = int(input("Player 2, please enter the y axis you want to start on: "))
                self.player2 = Player(self, player2_x, player2_y)
                player3_x = int(input("Player 3, please enter the x axis you want to start on: "))
                player3_y = int(input("Player 3, please enter the y axis you want to start on: "))
                self.player3 = Player(self, player3_x, player3_y)
                player4_x = int(input("Player 4, please enter the x axis you want to start on: "))
                player4_y = int(input("Player 4, please enter the y axis you want to start on: "))
                self.player4 = Player(self, player4_x, player4_y)
                self.all_sprites.add(self.player1, self.player2, self.player3, self.player4)
            else:
                player1_x = int(input("Player 1, please enter the x axis you want to start on: "))
                player1_y = int(input("Player 1, please enter the y axis you want to start on: "))
                self.player1 = Player(self, player1_x, player1_y)
                player2_x = int(input("Player 2, please enter the x axis you want to start on: "))
                player2_y = int(input("Player 2, please enter the y axis you want to start on: "))
                self.player2 = Player(self, player2_x, player2_y)
                self.all_sprites.add(self.player1, self.player2)        
        
             
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
                    self.player1.get_random()
                if event.key == pygame.K_RIGHT:
                    self.player2.get_random()

    def move_events(self, player_count):
        player1_move_count = 0
        player2_move_count = 0
        player3_move_count = 0
        player4_move_count = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                 self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player1.move(dx=-1)
                    player1_move_count += 1
                if event.key == pygame.K_RIGHT:
                    self.player1.move(dx=1)
                    player1_move_count += 1
                if event.key == pygame.K_UP:
                    self.player1.move(dy=-1)
                    player1_move_count += 1
                if event.key == pygame.K_DOWN:
                    self.player1.move(dy=1)
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
                if player_count > 2:
                    if event.key == ord('f'):
                        self.player3.move(dx=-1)
                        player3_move_count +=1
                    if event.key == ord('t'):
                        self.player3.move(dy=-1)
                        player3_move_count += 1
                    if event.key == ord('g'):
                        self.player3.move(dy=1)
                        player3_move_count += 1
                    if event.key == ord('h'):
                        self.player3.move(dx=1)        
                        player3_move_count += 1
                    if player_count > 3:
                        if event.key == ord('j'):
                            self.player4.move(dx=-1)
                            player4_move_count += 1
                        if event.key == ord('i'):
                            self.player4.move(dy=-1)
                            player4_move_count += 1
                        if event.key == ord('k'):
                            self.player4.move(dy=1)
                            player4_move_count += 1
                        if event.key == ord("l"):
                            self.player4.move(dx=1)        
                            player4_move_count += 1    
                    
    def hit(self):
        print("Hooray! You've met in the woods")
        #pygame.mixer.music.load('cheer.wav')

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
        g.new(2, grade_choice)
        g.run_random()
        print()
        
if grade_choice == "b" or grade_choice == "c":
    player_count = int(input("How many players would like to play? (max 4, min 2): "))
    while True:
        g.new(player_count, grade_choice)
        g.run(player_count)
        print()


    



    


"""
if __name__ =="__main__":
    main()"""