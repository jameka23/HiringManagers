import turtle
def draw_square():
    window = turtle.Screen() 
    window.bgcolor("yellow") #turns the shell's window yellow

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for x in range(1,5):
        brad.forward(100)
        brad.right(90)
    


    angie = turtle.Turtle() #init
    angie.shape("arrow")
    angie.color("black")
    angie.circle(100)

    
    billie = turtle.Turtle()
    billie.shape("classic")
    billie.color("purple")
    billie.forward(100)
    billie.right(45)
    billie.backward(100)
    billie.right(65)
    billie.forward(75)
    
    window.exitonclick()
draw_square()

