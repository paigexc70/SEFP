import turtle

# Ask the user for the size of the grid
size = int(input("Enter the size of the grid: "))

# Set up the Turtle window and pen
turtle.setup(500, 500)
pen = turtle.Turtle()
pen.speed(0)  # Set the pen speed to fastest

# Loop through each row of the grid
for y in range(size):
    # Draw the horizontal line
    pen.penup()
    pen.goto(0, y * 20)
    pen.pendown()
    pen.goto((size - 1) * 20, y * 20)

    # Draw the vertical line
    pen.penup()
    pen.goto(y * 20, 0)
    pen.pendown()
    pen.goto(y * 20, (size - 1) * 20)

# Keep the Turtle window open until it's manually closed
turtle.done()
