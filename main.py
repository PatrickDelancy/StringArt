import turtle
import random
from data import themes, build_wall_data
from drawing_functions import xIdx, yIdx, angleIdx, colorIdx, turtleIdx, init_wall_turtles, draw_wall, remove_wall, break_wall, draw_boundaries, boundary_size

wn = turtle.Screen()
wn.addshape("img/amongus.gif")
wn.addshape("img/kinda_sus.gif")
wn.addshape("img/broken_wall.gif")
wn.addshape("img/loading.gif")

wn.setup(boundary_size + 100, boundary_size + 100)

draw_boundaries()

selectedTheme = -1
while selectedTheme < 0 or selectedTheme > len(themes):
    print("Choose a color scheme from this list:\n\t1. Red\n\t2. Blue\n\t3. Yellow\n\t4. Christmas\n\t5. Halloween")
    selectedTheme = int(input("")) - 1

walls = build_wall_data(selectedTheme)

# Control variables
drawSpeed = 0
numberOfVisibleWalls = 4
move_increment = 3
keep_running = 1
line_index = 0

def collide_with_wall(idx):
    global walls
    wall = walls[idx]

    break_wall(wall)
    if idx < len(walls) - numberOfVisibleWalls:
        draw_wall(walls[idx + numberOfVisibleWalls])
    if (idx > 0):
        remove_wall(walls[idx - 1])

# "bounce" the ball off the obstacle, based on angle of the obstacle
def change_heading(heading, angle_of_obstacle):
    return (2 * angle_of_obstacle - heading + 360) % 360

wn.bgpic("img/loading.gif")
init_wall_turtles(walls)
wn.bgpic("")

#  draw first numberOfVisibleWalls walls
wallsDrawn = 0
while (wallsDrawn < numberOfVisibleWalls):
    wallsDrawn += 1
    draw_wall(walls[wallsDrawn])

traveller = turtle.Turtle(shape="circle")
traveller.penup()
traveller.pensize(3)
traveller.speed(drawSpeed)
traveller.goto(walls[0][xIdx], walls[0][yIdx])
traveller.setheading(walls[0][angleIdx])
traveller.pencolor(walls[0][colorIdx])
traveller.pendown()
nextWallIndex = 1

while (nextWallIndex < len(walls)):
    traveller.forward(move_increment)

    # have we hit a side?  This is an error condition
    if (abs(traveller.xcor()) >= boundary_size/2 or abs(traveller.ycor()) >= boundary_size/2):
        print("Error.  We missed a wall")
        exit()

    wall = walls[nextWallIndex]
    wallTurtle = wall[turtleIdx]

    currentDistance = int(traveller.distance(wallTurtle.pos()))
    if (currentDistance < 3):
        collide_with_wall(nextWallIndex)
        traveller.setheading(change_heading(
            traveller.heading(), wall[angleIdx]))
        if (wall[colorIdx] > ""):
            traveller.pencolor(wall[colorIdx])
            traveller.color(wall[colorIdx])

        nextWallIndex += 1
        currentDistance = 0
        lastDistance = 0

    lastDistance = currentDistance

# everything is drawn, remove the last wall
remove_wall(walls[len(walls)-1])

# random chance of having a suspicious character
if random.randint(1,50) % 2 == 0:
    traveller.setheading(150)
    traveller.penup()
    traveller.turtlesize(1)
    traveller.speed(1)
    traveller.shape("img/kinda_sus.gif")
    traveller.forward(150)
else:
    traveller.hideturtle()

if selectedTheme == 0:
    # This will draw the imposter on top of the string art
    imposter = turtle.Turtle()
    imposter.hideturtle()
    imposter.penup()
    imposter.speed(0)
    imposter.setheading(90)
    imposter.goto(100, 0)
    imposter.shape("img/amongus.gif")
    imposter.showturtle()

wn.mainloop()
