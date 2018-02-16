import turtle
def drawSq(the_turtle):
    for x in range(1,5):
        the_turtle.forward(100)
        the_turtle.right(90)
        
def draw_square():
    window = turtle.Screen() 
    window.bgcolor("yellow") #turns the shell's window yellow

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
 
    for i in range(1,36):
        drawSq(brad)
        brad.right(10)

    


##    angie = turtle.Turtle() #init
##    angie.shape("arrow")
##    angie.color("black")
##    angie.circle(100)
##
##    
##    billie = turtle.Turtle()
##    billie.shape("classic")
##    billie.color("purple")
##    billie.forward(100)
##    billie.right(45)
##    billie.backward(100)
##    billie.right(65)
##    billie.forward(75)
##    
    window.exitonclick()
draw_square()

