import turtle
turtle.Screen().bgcolor("Orange")

sc  = turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(10) :
  board.left(36)
  board.forward(100)
  i = i+1
board.hideturtle()
turtle.done()