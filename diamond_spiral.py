import turtle

def draw_scratch_pattern(limit=100):
    screen = turtle.Screen()
    screen.title("Scratch-inspired Pattern")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Point in direction 90° (east in Scratch) and go to (0,0)
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.clear()
    t.pendown()

    a = 0
    limit = 1000
    # repeat until a = 100
    while a <limit :
        # move a steps
        t.forward(a)
        # turn clockwise 121 degrees
        t.right(121)
        # move a steps
        t.forward(a)
        # turn clockwise 60 degrees
        t.right(60)
        # increment a by 1
        a += 1

    turtle.done()


if __name__ == "__main__":
    draw_scratch_pattern()
