from turtle import *
import random

# parameters
width = 500
height = 800

# general setup
setup(width, height)
tracer(0, 0)
bgcolor('white')

# color list
colors = ['blue', 'red', 'violet', 'black', 'orange', 'green', 'yellow']

# rectangle (top left)
penup()
goto(-150, 100)
pendown()
fillcolor(random.choice(['red', 'violet', 'blue']))
begin_fill()
for i in range(4):
    if i % 2 == 0:
        forward(200)
    else:
        forward(120)
    right(90)
end_fill()

# first circle
penup()
goto(-100, 120)
pendown()
fillcolor(random.choice(['red', 'orange', 'yellow']))
begin_fill()
circle(80)
end_fill()

# second circle
penup()
goto(100, -170)
pendown()
fillcolor(random.choice(['green', 'yellow', 'orange', 'red']))
begin_fill()
circle(80)
end_fill()

# small square
penup()
goto(100, -150)
pendown()
fillcolor(random.choice(['blue', 'black', 'purple']))
begin_fill()
for i in range(4):
    forward(120)
    right(90)
end_fill()

# spiral (center)
spiral_positions = [-150, 0, 150]

penup()
goto(0, -150)
pendown()
pencolor('black')
for i in range(150):
    forward(i * 0.5)
    right(91)

for s in spiral_positions:
    penup()
    goto(s, -100)
    pendown()
    for i in range(100):
        forward(i * 0.5)
        right(91)

update()
done()
