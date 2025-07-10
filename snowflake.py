import turtle

def koch_curve(t, order, size):
    """Draws a single Koch curve segment."""
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)
        t.right(120)
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)

def draw_snowflake(t, order, size):
    """Draws and fills a full Koch snowflake (3 Koch curves)."""
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    t.end_fill()

def setup():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("skyblue")
    screen.title("Turtle Koch Snowflake")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)
    t.color("white")      # outline color
    return screen, t

def main():
    screen, t = setup()
    t.penup()
    # center the snowflake
    t.goto(-200, 100)
    t.pendown()
    # draw a level-4, filled snowflake of side length 400
    draw_snowflake(t, order=4, size=400)
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()
