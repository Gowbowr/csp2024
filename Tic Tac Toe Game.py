import turtle

# Create screen
screen = turtle.Screen()
screen.title("Tic-Tac-Toe")
screen.bgpic("giphy.gif")
screen.setup(width=800, height=800)

# Create turtle object for drawing
painter = turtle.Turtle()
painter.speed(0)
painter.pensize(5)
painter.hideturtle()

# Take color input from players
P1 = input("Choose a color Player 1 (X): ")
P2 = input("Choose a color Player 2 (O): ")

# Draw Tic-Tac-Toe grid
painter.pensize(15)
painter.penup()
painter.goto(-300, 100)
painter.pendown()
painter.goto(300, 100)
painter.penup()
painter.goto(-300, -100)
painter.pendown()
painter.goto(300, -100)
painter.penup()
painter.goto(-100, 300)
painter.pendown()
painter.goto(-100, -300)
painter.penup()
painter.goto(100, 300)
painter.pendown()
painter.goto(100, -300)
painter.penup()

# Draw X
def draw_x(x, y):
    painter.color(P1)  # Use Player 1's chosen color
    painter.penup()
    painter.goto(x - 50, y - 50)
    painter.pendown()
    painter.goto(x + 50, y + 50)
    painter.penup()
    painter.goto(x + 50, y - 50)
    painter.pendown()
    painter.goto(x - 50, y + 50)

# Draw O
def draw_o(x, y):
    painter.color(P2)  # Use Player 2's chosen color
    painter.penup()
    painter.goto(x, y - 50)
    painter.pendown()
    painter.circle(50)

# Handle mouse click event
def click_handler(x, y):
    if x < -100:
        col = 0
    elif x < 100:
        col = 1
    else:
        col = 2

    if y > 100:
        row = 0
    elif y > -100:
        row = 1
    else:
        row = 2

    x_pos = -200 + col * 200
    y_pos = 200 - row * 200

    if col % 2 == 0:
        draw_x(x_pos, y_pos)
    else:
        draw_o(x_pos, y_pos)

# Set up the click handler
screen.listen()
screen.onscreenclick(click_handler)

# Keep the window open
turtle.done()


