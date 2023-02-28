# This is a program to simulate Wandering in the Woods game

# Import necessary libraries
import random
import time

# Define the game board
def create_board(x, y):
    board = []
    for i in range(x):
        board.append([])
        for j in range(y):
            board[i].append(0)
    return board

# Define players
def create_players(board, num_players):
    players = []
    for i in range(num_players):
        x = random.randint(0, len(board)-1)
        y = random.randint(0, len(board[0])-1)
        players.append([x, y])
    return players

# Define the players' moves
def move_player(board, players, player_num):
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    if (players[player_num][0] + x < 0 or players[player_num][0] + x > len(board)-1):
        x = 0
    if (players[player_num][1] + y < 0 or players[player_num][1] + y > len(board[0])-1):
        y = 0

    players[player_num][0] += x
    players[player_num][1] += y

# Check if players meet
def check_meet(players, player_num):
    if (players[player_num] in players[:player_num]):
        return True
    else:
        return False

# Main game loop
def play_game(board, players, num_players):
    move_count = 0
    meet = False
    while (not meet):
        for i in range(num_players):
            move_player(board, players, i)
            move_count += 1
            meet = check_meet(players, i)
            if (meet):
                break
        time.sleep(0.1)

    return move_count

# Run the game
x = int(input("Enter the width of the board: "))
y = int(input("Enter the height of the board: "))
num_players = int(input("Enter the number of players: "))

board = create_board(x, y)
players = create_players(board, num_players)

move_count = play_game(board, players, num_players)

print("The players met after {} moves".format(move_count))