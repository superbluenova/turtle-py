#!/usr/bin/env python3
"""
Café Wall Illusion

This script uses turtle graphics to draw the Café Wall illusion: rows of
black and white squares offset every other row, with gray mortar between
the tiles, causing the horizontal lines to appear sloped.
"""

import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Café Wall Illusion")
screen.bgcolor("lightgray")  # Mortar color

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Configuration
rows = 12              # Number of rows of tiles
cols = 16              # Number of tiles per row
tile_size = 40         # Size of each square tile
mortar = 2             # Gap between tiles (mortar width)
offset = tile_size // 2 + mortar // 2  # Offset for alternating rows

# Starting top-left position
start_x = - (cols * (tile_size + mortar)) / 2
start_y = (rows * (tile_size + mortar)) / 2

# Draw tiles
for row in range(rows):
    y = start_y - row * (tile_size + mortar)
    for col in range(cols):
        # Compute x with alternating offset
        x = start_x + col * (tile_size + mortar)
        if row % 2 == 1:
            x += offset
        # Choose color: black for even columns, white for odd
        color = "black" if col % 2 == 0 else "white"
        # Draw square tile
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(color)
        t.pencolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(tile_size)
            t.right(90)
        t.end_fill()

# Finish
turtle.done()
