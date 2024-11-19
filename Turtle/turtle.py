import turtle 

turtle.Screen().bgcolor("Red")

sc= turtle.Screen()
sc.setup(400,300)
turtle.title("Turtle Window")

t= turtle.Turtle()

for i in range(4):
    t.forward(125)
    t.left(90)

turtle.done()