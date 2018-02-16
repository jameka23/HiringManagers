import turtle
def draw_square():
    window = turtle.Screen() 
    window.bgcolor("yellow") #turns the shell's window yellow

    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()
draw_square()
