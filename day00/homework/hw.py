import turtle

# ეკრანისა და კუს შექმნა
screen = turtle.Screen()
pen = turtle.Turtle()

# კუს სიჩქარის დაყენება (0 არის ყველაზე სწრაფი)
pen.speed(0)

# სახლის ძირი
pen.pendown()
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(50)

# სახლის სახურავი
pen.right(45)
pen.forward(70)
pen.left(90)
pen.forward(70)

# ფანჯარა
pen.penup()
pen.goto(30, 20)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for i in range(4):
    pen.forward(20)
    pen.right(90)
pen.end_fill()

# კუს დამალვა
pen.hideturtle()

turtle.done()