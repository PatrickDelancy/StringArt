import turtle

xIdx = 0
yIdx = 1
angleIdx = 2
colorIdx = 3
turtleIdx = 4

boundary_size = 500

# method to draw the bounding box
def draw_boundaries():
  global boundary_size

  boundary_pen = turtle.Turtle()
  boundary_pen.speed(0)
  boundary_pen.pensize(5)
  boundary_pen.penup()
  # position to upper left corner
  boundary_pen.goto(-boundary_size/2, boundary_size/2)
  boundary_pen.pendown()
  sides_drawn = 0
  while (sides_drawn < 4):
    boundary_pen.forward(boundary_size)  
    boundary_pen.right(90)
    sides_drawn += 1
  boundary_pen.hideturtle()


def init_wall_turtles(walls):
  for wall in walls:
    mason = turtle.Turtle()
    mason.hideturtle()
    mason.speed(0)
    mason.pensize(4)
    mason.penup()
    mason.goto(wall[xIdx], wall[yIdx])
    mason.setheading(wall[angleIdx])

    if (wall[colorIdx] != ""):
      mason.pencolor(wall[colorIdx])  
    
    wall.append(mason)

def draw_wall(wall):
  mason = wall[turtleIdx]

  mason.backward(25)
  mason.pendown()
  mason.forward(50)
  mason.backward(25)

def break_wall(wall):
  mason = wall[turtleIdx]
  mason.clear()
  mason.shape("img/broken_wall.gif")
  mason.showturtle()

def remove_wall(wall):
  if (len(wall) > turtleIdx):
    mason = wall[turtleIdx]
    mason.hideturtle()
    mason.clear()
    del wall[turtleIdx]
