# This program allows two people to wander in the woods and meet up, with different levels of complexity for different grades.

# Imports
import random

#Grid Setup
def setup_grid(K_2, grades_3_5, grades_6_8):
  #For grades K-2, the grid is always square and the people start out in diagonally opposite corners
  if K_2:
    grid_size = int(input("Please enter the size of the grid: "))
    p1_x = 0
    p1_y = 0
    p2_x = grid_size - 1
    p2_y = grid_size - 1
  #For grades 3-5, students can set up the size of a grid, which can be rectangular
  elif grades_3_5:
    grid_width = int(input("Please enter the width of the grid: "))
    grid_height = int(input("Please enter the height of the grid: "))
    p1_x = int(input("Please enter the x-coordinate of Person 1: "))
    p1_y = int(input("Please enter the y-coordinate of Person 1: "))
    p2_x = int(input("Please enter the x-coordinate of Person 2: "))
    p2_y = int(input("Please enter the y-coordinate of Person 2: "))
  #For grades 6-8, students can set up the size of a grid, which can be rectangular, and can include 2, 3, or 4 people
  elif grades_6_8:
    grid_width = int(input("Please enter the width of the grid: "))
    grid_height = int(input("Please enter the height of the grid: "))
    num_people = int(input("Please enter the number of people: "))
    p1_x = int(input("Please enter the x-coordinate of Person 1: "))
    p1_y = int(input("Please enter the y-coordinate of Person 1: "))
    if num_people > 2:
      p2_x = int(input("Please enter the x-coordinate of Person 2: "))
      p2_y = int(input("Please enter the y-coordinate of Person 2: "))
    if num_people > 3:
      p3_x = int(input("Please enter the x-coordinate of Person 3: "))
      p3_y = int(input("Please enter the y-coordinate of Person 3: "))
    if num_people > 4:
      p4_x = int(input("Please enter the x-coordinate of Person 4: "))
      p4_y = int(input("Please enter the y-coordinate of Person 4: "))
  
  # Create the grid
  grid = [[0] * grid_width for _ in range(grid_height)]
  
  # Place the people on the grid
  grid[p1_x][p1_y] = 1
  grid[p2_x][p2_y] = 2
  if num_people > 2:
    grid[p3_x][p3_y] = 3
  if num_people > 3:
    grid[p4_x][p4_y] = 4
  
  return grid

#Person Movement
def move_people(grid):
  # Get the number of people
  num_people = 0
  for row in grid:
    for item in row:
      if item > 0:
        num_people += 1
  
  # Move each person
  for person in range(1, num_people+1):
    # Find the person's current position
    for row in range(len(grid)):
      for col in range(len(grid[row])):
        if grid[row][col] == person:
          current_x = row
          current_y = col
    
    # Generate a random move
    direction = random.randint(1, 4)
    if direction == 1:  # Up
      new_x = max(0, current_x - 1)
    elif direction == 2:  # Down
      new_x = min(len(grid) - 1, current_x + 1)
    elif direction == 3:  # Left
      new_y = max(0, current_y - 1)
    elif direction == 4:  # Right
      new_y = min(len(grid[0]) - 1, current_y + 1)
    
    # Move the person
    grid[current_x][current_y] = 0
    grid[new_x][new_y] = person

#Check for a collision
def check_for_collision(grid):
  # Check for a collision
  collision = False
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] > 1:
        collision = True
  return collision

#Statistics
def display_statistics(num_moves):
  # Display the statistics
  print("The people met after {} moves.".format(num_moves))

#Main Function
def main():
  # Get the grade level
  K_2 = False
  grades_3_5 = False
  grades_6_8 = False
  grade = int(input("Please enter your grade: "))
  if grade >= 0 and grade <= 2:
    K_2 = True
  elif grade >= 3 and grade <= 5:
    grades_3_5 = True
  elif grade >= 6 and grade <= 8:
    grades_6_8 = True
  
  # Set up the grid
  grid = setup_grid(K_2, grades_3_5, grades_6_8)
  
  # Move the people
  num_moves = 0
  collision = False
  while not collision:
    move_people(grid)
    num_moves += 1
    collision = check_for_collision(grid)
  
  # Display the statistics
  display_statistics(num_moves)

# Run the program
if __name__ == "__main__":
  main()