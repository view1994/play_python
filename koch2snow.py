import turtle

def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        koch(size/3,n-1)
        turtle.left(60)
        koch(size / 3, n - 1)
        turtle.right(120)
        koch(size/3,n-1)
        turtle.left(60)
        koch(size/3,n-1)
def drew_snow(size,n=2):
    koch(size,n)
    turtle.right(120)
    koch(size,n)
    turtle.right(120)
    koch(size,n)

def main():
    turtle.setup(1000,800)
    turtle.speed(10)
    turtle.pensize(5)
    turtle.pu()
    turtle.goto(-400,200)
    turtle.pd()
    drew_snow(300,3)
    turtle.done()
if __name__ == '__main__':
    main()