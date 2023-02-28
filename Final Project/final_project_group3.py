import random

# Set the size of the grid
GRID_SIZE = 10

# Set the starting positions of the two players
player1_pos = (0, 0)
player2_pos = (GRID_SIZE-1, GRID_SIZE-1)

# Initialize the move counters for the two players
player1_moves = 0
player2_moves = 0

# Play the game until the players meet each other
while player1_pos != player2_pos:
    # Move player 1 randomly
    player1_pos = (player1_pos[0] + random.choice([-1, 0, 1]), player1_pos[1] + random.choice([-1, 0, 1]))
    # Make sure player 1 stays within the grid
    player1_pos = (min(max(player1_pos[0], 0), GRID_SIZE-1), min(max(player1_pos[1], 0), GRID_SIZE-1))
    # Increment player 1's move counter
    player1_moves += 1

    # Move player 2 randomly
    player2_pos = (player2_pos[0] + random.choice([-1, 0, 1]), player2_pos[1] + random.choice([-1, 0, 1]))
    # Make sure player 2 stays within the grid
    player2_pos = (min(max(player2_pos[0], 0), GRID_SIZE-1), min(max(player2_pos[1], 0), GRID_SIZE-1))
    # Increment player 2's move counter
    player2_moves += 1

# Display the statistics of the game
print("Players met each other after", player1_moves, "moves.")

