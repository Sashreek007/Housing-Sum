import turtle

# Function to draw a rectangle with given color and dimensions
def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Set up the screen
turtle.setup(width=600, height=400)
turtle.title("Pride Ligga")

# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# Draw the rectangle with pride colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
width = 50
height = 200
for color in colors:
    draw_rectangle(color, width, height)
    turtle.forward(width)
    
# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
