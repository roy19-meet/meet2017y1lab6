UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
##################
def up():
    global direction
    old_pos=turtle.pos()
    x=old_pos[0]
    print('you pressed up')
def down():
    global direction
    direction = DOWN
    print('you pressed down') 
def left():
    global direction
    direction = LEFT
    print('you pressed left') 
def right():
    global direction
    direction = RIGHT
    print('you pressed right')
################################    
import turtle
UP=0
LEFT=1
DOWN=2
RIGHT=3
direction=UP
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

turtle.mainloop()

##

    
