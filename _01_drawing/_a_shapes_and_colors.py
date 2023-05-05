import turtle

if __name__ == '__main__':
    window = turtle.Screen


    # This code makes a new Turtle. Pick a new name for the turtle
    my_kirk = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    my_kirk.shape('turtle')

    # Set your turtle's speed using .speed(2)
    my_kirk.speed(2)

    # Set your turtle's color using .color('green') and .pencolor('blue')
    # my_kirk.color('orange')
    # my_kirk.pencolor('bule')
    #
    # # Move your turtle forward using .forward(100)
    # # TEST    Did your turtle move forward?
    # # my_kirk.forward(100)
    #
    # # Move your turtle left or right using .left(90) or .right(90)
    # # my_kirk.right(90)
    # # Now put the forward and left/right code into a for loop to repeat 4 times.
    # # TEST    Did your turtle draw a square?
    # my_kirk.begin_fill()
    for i in range (4):
        my_kirk.forward(100)
        my_kirk.forward(10)
    # my_kirk.end_fill()
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    # my_kirk.goto(100,99)
    # my_kirk.goto(100,-99)
    # my_kirk.color('pink')
    # my_kirk.pencolor('red')
    # # Have your turtle draw a circle using .circle(radius, steps=30)
    # # TEST    Did your turtle draw a circle?
    # my_kirk.begin_fill()
    # my_kirk.circle(100,steps=100)
    # # Add color to your shape by adding .begin_fill() before drawing the circle
    # my_kirk.end_fill()
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    # my_kirk.goto(-100,100)
    my_kirk.forward(80)
    my_kirk.left(90)
    my_kirk.forward(80)
    my_kirk.right(90)
    my_kirk.forward(80)
    my_kirk.left(90)
    my_kirk.forward(80)
    my_kirk.right(90)
    my_kirk.forward(80)
    my_kirk.right(90)
    my_kirk.forward(80)
    my_kirk.left(90)
    my_kirk.forward(80)
    my_kirk.right(90)
    my_kirk.forward(80)
    my_kirk.right(90)
    my_kirk.forward(100)
    my_kirk.forward(200)
    my_kirk.right(90)
    my_kirk.forward(200)
    my_kirk.left(90)
    my_kirk.right(80)
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
