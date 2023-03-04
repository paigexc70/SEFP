import pygame, sys
from pygame.locals import *
import random
import os
from player import Player
from settings import *


all_sprites = pygame.sprite.Group()


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
    
    def update(self):
        self.all_sprites.update()   
        
        
    def quit(self):
        play_again = input('Play again (y or n)? ')
        if play_again == "y":
            pygame.quit()
            __main__()
        else:
            print("Thank you for playing!")
            pygame.quit()
            sys.exit()
            
    def hit(self):
        print("Hooray! You've all met in the woods!")
        pygame.mixer.music.load('cheer.wav')
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(0)
        
                
    def x_y_tester(self,x, y):
        if x > GRID_SIZE_LENGHT:
            x = GRID_SIZE_LENGHT - 1
        if y > GRID_SIZE_HEIGHT:
            y = GRID_SIZE_HEIGHT - 1
        return [x,y]
            
        
    def play_again(self):
        play_again = False
        play_again = input("Would you like to play again? (y or n): ")
        play_again = play_again.lower()
        while play_again != "y" or play_again != "n":
            play_again = input("Would you like to play again? (y or n): ")
            play_again = play_again.lower()
        if play_again == "y":
            play_again = True
        else:
            play_again = False
        return play_again
            
        
    def run_random(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(self.FPS)
            self.random_events()
            self.draw("a", 9,9)
            self.update()
           
           
    def run(self, player_count, grade_choice):
        if grade_choice == "a":
            self.playing = True
            while self.playing:
                pygame.display.update()
                pygame.mixer.music.load('music.wav')
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.dt = self.clock.tick(self.FPS)
                self.draw(grade_choice)
                self.move_events(player_count)
                self.update()
        elif grade_choice == "b" or grade_choice == "c":
            GRID_SIZE_LENGHT = int(input("How long would you like the grid to be: "))
            GRID_SIZE_HEIGHT = int(input("How tall would you like the grid to be: "))
            WINDOW_SIZE = (GRID_SIZE_LENGHT * CELL_SIZE, GRID_SIZE_HEIGHT * CELL_SIZE)
            self.DISPLAYSURF = pygame.display.set_mode((WINDOW_SIZE), pygame.RESIZABLE)
            self.playing = True
            while self.playing:
                pygame.mixer.music.load('music.wav')
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                self.dt = self.clock.tick(self.FPS) 
                self.update()
                self.draw(grade_choice,GRID_SIZE_LENGHT, GRID_SIZE_HEIGHT)
                self.move_events(player_count)
                pygame.display.update()
                
            
    def draw(self, grade_choice, lenght, height):
        if grade_choice == "a":
            self.DISPLAYSURF.fill(BGCOLOR)
            self.draw_grid()
            self.all_sprites.draw(self.DISPLAYSURF)
            pygame.display.flip()
        elif grade_choice == "b" or grade_choice == "c":
            self.DISPLAYSURF.fill(BGCOLOR)
            self.draw_grid(lenght, height)
            self.all_sprites.draw(self.DISPLAYSURF)
            pygame.display.flip()   
        
    def draw_grid(self, lenght = 10, height = 10):
        for x in range(0, lenght * CELL_SIZE, CELL_SIZE):
            for y in range(0, height * CELL_SIZE, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.DISPLAYSURF, WHITE, rect, 1) 
        
        
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
                player1_pair = self.x_y_tester(player1_x, player1_y)
                self.player1 = Player(self, player1_pair[0], player1_pair[1])
                player2_x = int(input("Player 2, please enter the x axis you want to start on: "))
                player2_y = int(input("Player 2, please enter the y axis you want to start on: "))
                player2_pair = self.x_y_tester(player2_x, player2_y)
                self.player2 = Player(self, player2_pair[0], player2_pair[1])
                player3_x = int(input("Player 3, please enter the x axis you want to start on: "))
                player3_y = int(input("Player 3, please enter the y axis you want to start on: "))
                player3_pair = self.x_y_tester(player3_x, player3_y)
                self.player3 = Player(self, player3_pair[0], player3_pair[1])
                self.all_sprites.add(self.player1, self.player2, self.player3) 
            elif player_count == 4:
                player1_x = int(input("Player 1, please enter the x axis you want to start on: "))
                player1_y = int(input("Player 1, please enter the y axis you want to start on: "))
                player1_pair = self.x_y_tester(player1_x, player1_y)
                self.player1 = Player(self, player1_pair[0], player1_pair[1])
                player2_x = int(input("Player 2, please enter the x axis you want to start on: "))
                player2_y = int(input("Player 2, please enter the y axis you want to start on: "))
                player2_pair = self.x_y_tester(player2_x, player2_y)
                self.player2 = Player(self, player2_pair[0], player2_pair[1])
                player3_x = int(input("Player 3, please enter the x axis you want to start on: "))
                player3_y = int(input("Player 3, please enter the y axis you want to start on: "))
                player3_pair = self.x_y_tester(player3_x, player3_y)
                self.player3 = Player(self, player3_pair[0], player3_pair[1])
                player4_x = int(input("Player 4, please enter the x axis you want to start on: "))
                player4_y = int(input("Player 4, please enter the y axis you want to start on: "))
                player4_pair = self.x_y_tester(player4_x, player4_y)
                self.player4 = Player(self, player4_pair[0], player4_pair[1])
                self.all_sprites.add(self.player1, self.player2, self.player3, self.player4)
            else:
                player1_x = int(input("Player 1, please enter the x axis you want to start on: "))
                player1_y = int(input("Player 1, please enter the y axis you want to start on: "))
                player1_pair = self.x_y_tester(player1_x, player1_y)
                self.player1 = Player(self, player1_pair[0], player1_pair[1])
                player2_x = int(input("Player 2, please enter the x axis you want to start on: "))
                player2_y = int(input("Player 2, please enter the y axis you want to start on: "))
                player2_pair = self.x_y_tester(player2_x, player2_y)
                self.player2 = Player(self, player2_pair[0], player2_pair[1])
                self.all_sprites.add(self.player1, self.player2)        
                

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
                self.checkCollision(2)
                

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
                self.checkCollision(player_count)    
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
                    self.checkCollision(player_count)
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
                        self.checkCollision(player_count)
                        
            
    def checkCollision(self, player_count):
        if player_count == 2:
            if self.player2.x == self.player1.x and self.player2.y == self.player1.y:
                self.player2.x = self.player2.y = -100
                self.hit()
                self.quit()
        elif player_count == 3: 
            if (self.player2.x == self.player1.x != -100) and (self.player2.y == self.player1.y != -100):
                self.player2.x = self.player2.y = -100
                print("Player 2 collided with player 1! You guys will now travel together using player 1's controls.")
            if (self.player3.x == self.player1.x != -100) and (self.player3.y == self.player1.y != -100):
                self.player3.x = self.player3.y = -100
                print("Player 3 collided with player 1! You guys will now travel together using player 1's controls.")
            if (self.player3.x == self.player2.x != -100) and (self.player3.y == self.player2.y != -100):
                self.player3.x = self.player3.y = -100
                print("Player 3 collided with player 2! You guys will now travel together using player 2's controls.")
            if self.player2.x == self.player2.y == self.player3.x == self.player3.y == -100:
                self.player1.x = self.player1.y = -100
                if self.player2.x == self.player2.y == self.player3.x == self.player3.y == self.player1.x == self.player1.y == -100:
                    self.hit()
                    self.quit()
        elif player_count == 4:
            if (self.player2.x == self.player1.x != -100) and (self.player2.y == self.player1.y != -100):
                self.player2.x = self.player2.y = -100
                print("Player 2 collided with player 1! You guys will now travel together using player 1's controls.")
            if (self.player3.x == self.player1.x != -100) and (self.player3.y == self.player1.y != -100):
                self.player3.x = self.player3.y = -100
                print("Player 3 collided with player 1! You guys will now travel together using player 1's controls.")
            if (self.player3.x == self.player2.x != -100) and (self.player3.y == self.player2.y != -100):
                self.player3.x = self.player3.y = -100
                print("Player 3 collided with player 2! You guys will now travel together using player 2's controls.")
            if (self.player4.x == self.player3.x != -100) and (self.player4.y == self.player3.y != -100):
                self.player4.x = self.player4.y = -100
                print("Player 4 collided with player 3! You guys will now travel together using player 3's controls.")
            if (self.player4.x == self.player2.x != -100) and (self.player4.y == self.player2.y != -100):
                self.player4.x = self.player4.y = -100
                print("Player 4 collided with player 2! You guys will now travel together using player 2's controls.")
            if (self.player4.x == self.player1.x != -100) and (self.player4.y == self.player1.y != -100):
                self.player4.x = self.player4.y = -100
                print("Player 4 collided with player 1! You guys will now travel together using player 1's controls.")
            if self.player2.x == self.player2.y == self.player3.x == self.player3.y  == self.player4.x == self.player4.y == -100:
                self.player1.x = self.player1.y = -100
                if self.player2.x == self.player2.y == self.player3.x == self.player3.y  == self.player4.x == self.player4.y == self.player1.x == self.player1.y == -100:
                    self.hit()
                    self.quit()
                



def __main__():
    g = Game()
    grade_choice = ""
    print("A. K - 2")
    print("B. 3 - 5")
    print("C. 6 - 8")
    grade_choice = input("What grade level would you like to play: ")
    grade_choice = grade_choice.lower()
    while grade_choice != "a" and grade_choice != "b" and grade_choice != "c":
        grade_choice = input("What grade level would you like to play: ")
        grade_choice = grade_choice.lower()
        
    while True:
        if grade_choice == "a":
            g.new(2, grade_choice)
            g.run_random()
            
        elif grade_choice == "b" or grade_choice == "c":
            player_count = int(input("How many players would like to play? (max 4, min 2): "))
            while player_count != 2 and player_count != 3 and player_count != 4:
                player_count = int(input("How many players would like to play? (max 4, min 2): "))
            g.new(player_count, grade_choice)    
            g.run(player_count, grade_choice)
            
           
            



if __name__ =="__main__":
    __main__()


    
