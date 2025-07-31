import turtle

"""
result = turtle.pos()  # Get the current position of the turtle
turtle.pensize(5)  # Set the pen size to 5
turtle.pencolor("blue")  # Set the pen color to blue
result = turtle.goto(100, 100)  # Move the turtle to a specific position
pos = turtle.position()  # Another way to get the current position
print(pos)
turtle.setposition(-50, 50)  # Set the turtle's position to (-50, 50)
turtle.setpos(-50, -50)  # Set the turtle's position to (-50, 50)
turtle.setposition(0, 0)  # Set the turtle's position to the origin (0, 0)
turtle.reset()  # Reset the turtle to its initial state
turtle.home()  # Move the turtle to the home position (0, 0)
turtle.begin_fill()  # Begin filling a shape
tuttle.color("red,blue")  # Set the turtle color to red
turtle.end_fill()  # End filling a shape
turtle.fillcolor("red")  # Set the fill color to red
"""

# uygulama  1
""""

turtle.title("Turtle Position Example")  # Set the window title
turtle.shape("turtle")  # Set the turtle shape
turtle.speed(1)  # Set the turtle speed to slow
turtle.setpos(50, 100)  # Move the turtle to (0, 100)
turtle.goto(-200, 200)  # Move the turtle 
turtle.home()  # Move the turtle to the home position (0, 0)
turtle.setx(100)  # Set the turtle's x-coordinate to 100
turtle.sety(-100)  # Set the turtle's y-coordinate to -100
"""

# uygulama 2
turtle.title("Turtle Position Example")  # Set the window title
turtle.shape("turtle")  # Set the turtle shape
turtle.speed(1)  # Set the turtle speed to slow
# turtle.penup()  # Lift the pen to avoid drawing while moving    
turtle.forward(100)  # Move the turtle forward by 100 units
turtle.fd(50)  # Move the turtle forward by 50 units
turtle.backward(50)  # Move the turtle backward by 50 units
turtle.bk(100)  # Move the turtle backward by 100 units
turtle.right(90)  # Turn the turtle right by 90 degrees
turtle.fd(50)  # Move the turtle forward by 50 units
turtle.left(45)  # Turn the turtle left by 45 degrees   
turtle.bk(30)  # Move the turtle backward by 30 units
turtle.setheading(0)  # Set the turtle's heading to 0 degrees (facing right)
turtle.home()  # Move the turtle to the home position (0, 0)
# turtle.mainloop()  # Keep the turtle graphics window open
print(turtle.getshapes())  # Print the available turtle shapes 
# ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
turtle.done()  # Finish the turtle graphics
