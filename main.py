import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

#Part A):
def drawSineCurve(dart):
    for x in range(-360, 361):
      y = math.sin(math.radians(x))
      dart.color("red")
      dart.goto(x, y)
    dart.up()
    


#Part B):



def setupWindow(wn=None):
    wn.setworldcoordinates(-360, -1, 360, 1)


def drawCosineCurve(dart):
  dart.goto(-360, 1)
  dart.down()
  for x in range(-360, 361):
      y = math.cos(math.radians(x))
      dart.color("green")
      dart.goto(x, y)
  dart.up()


def drawTangentCurve(dart):
    dart.goto(-360, 0)
    dart.down()  
    for x in range(-360, 361):
      y = math.tan(math.radians(x))
      dart.color("blue")
      dart.goto(x, y)
    dart.up()


def setupAxis(dart = None):
  dart.up()
  dart.goto(-360, 0)
  dart.down()
  dart.goto(360, 0)
  dart.up()
  dart.goto(0, -1)
  dart.down()
  dart.goto(0, 1)
  dart.up()
  dart.goto(-360, 0)
  dart.down()




##########  Do Not Alter Any Code Past Here ########

def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()