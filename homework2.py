import turtle
turtle.Screen().bgcolor("Orange")

sc  = turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(5) :
  board.left(72)
  board.forward(200)
  i = i+1
board.hideturtle()
turtle.done()