import turtle

def setup_screen(width=800, height=800, bgcolor="#ffffff", title="Mandala Design"):
    """Initialize the drawing screen."""
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.bgcolor(bgcolor)
    screen.title(title)
    return screen

def setup_turtle(speed=0, pensize=2):
    """Initialize the turtle."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(speed)
    t.pensize(pensize)
    return t

def draw_background_rings(t, radii, colors):
    """Draw filled concentric rings from outermost to innermost."""
    for r, color in zip(radii, colors):
        t.penup()
        t.goto(0, -r)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()

def draw_petal(t, radius, extent, color):
    """Draw a single petal as two arcs."""
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, extent)
    t.left(180 - extent)
    t.circle(radius, extent)
    t.left(180 - extent)
    t.end_fill()

def draw_layer(t, count, radius, extent, color):
    """Draw a ring of petals around the center."""
    angle = 360 / count
    for _ in range(count):
        draw_petal(t, radius, extent, color)
        t.left(angle)

def main():
    screen = setup_screen()
    t = setup_turtle(pensize=1)

    # 1) Background: filled rings
    ring_radii  = [220, 165, 100, 50]                          # outer to inner
    ring_colors = ["#e76f51", "#f4a261", "#2a9d8f", "#264653"]  # palette inverted
    draw_background_rings(t, ring_radii, ring_colors)

    # 2) Move to center for petals
    t.penup()
    t.goto(0, 0)
    t.pendown()

    # 3) Draw successive petal layers
    petal_colors = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
    draw_layer(t, count=8,  radius=200, extent=60, color=petal_colors[0])
    draw_layer(t, count=12, radius=140, extent=50, color=petal_colors[1])
    draw_layer(t, count=16, radius= 80, extent=40, color=petal_colors[2])
    draw_layer(t, count=20, radius= 40, extent=30, color=petal_colors[3])

    # 4) Central circle
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.fillcolor(petal_colors[4])
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    screen.exitonclick()

if __name__ == "__main__":
    main()
