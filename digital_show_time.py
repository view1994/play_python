import turtle
import time
seg_tab=[0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
def drew_num(n,numsize=40,color='black',pensize=5,x=0,y=0):
    seg=seg_tab[n]
    start=turtle.position()
    turtle.pu()
    #turtle.goto(x,y)
    turtle.seth(0)
    turtle.pencolor(color)
    turtle.pensize(pensize)
    for i in range(7):
        if seg&(1<<i):
            turtle.pd()
        else:
            turtle.pu()
        turtle.fd(numsize)
        if i in [1,4]:
            pass
        elif i==5:
            turtle.pu()
            turtle.fd(-numsize)
            turtle.right(90)
        else:
            turtle.right(90)
    turtle.pu()
    turtle.goto(start)
    turtle.seth(0)
    turtle.fd(numsize+10)
def drew_str(str,numsize=40,color='black',pensize=5,x=0,y=0):
    turtle.pu()
    turtle.goto(x,y)
    for i in str:
        if i in '0123456789':
            drew_num(eval(i),color=color,pensize=pensize,x=x,y=y)
        else:
            turtle.pu()
            turtle.seth(-90)
            turtle.fd(numsize)
            turtle.left(90)
            turtle.pencolor('blue')
            turtle.write(i,font=('Arial',18,'normal'))
            turtle.fd(numsize+10)
            turtle.seth(90)
            turtle.fd(numsize)

if __name__=='__main__':
    turtle.setup(1000,400)
    turtle.speed(10)
    #turtle.hideturtle()
    t=time.strftime('%Y年%m月%d日',time.gmtime())
    print(t)
    turtle.pu()
    turtle.fd(-500)
    x, y = -100, 100
    drew_str(t,color='red',pensize=8,x=x,y=y)
    turtle.done()