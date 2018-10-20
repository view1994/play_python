from turtle import *
import time
# write a word "shi" by turtle
color("red")
# pen up, don't draw
up()
# centers the circle
goto(0, -50)
# pen down, draw
down()
# radius=50  center is 50 radius units above the turtle
#circle(50)
up()
# center the turtle again
goto(0, 0)
down()

# draw blue 100x100 squares
#color("")
right(45)
forward(10 * 1.414)
up()

goto(-5, -20)
down()
right(-50)
forward(20)
right(95)
forward(50)
right(-90-45)
forward(25)
up()

goto(40, -10)           #right
down()
right(45)
forward(35)
up()

goto(60, 10)            #down
down()
right(90)
forward(35)
up()

goto(30, -25)           #right
down()
right(-90)
forward(55)
up()

goto(30, -40)           #right
down()
right(0)
forward(60)
up()

goto(75, -30)            #down
down()
right(90)
forward(45)
         #left&up30
right(90+30)
forward(25)
up()

goto(44, -44)           #right
down()
right(180)
forward(25)
up()

time.sleep(5)