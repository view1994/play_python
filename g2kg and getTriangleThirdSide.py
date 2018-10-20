#coding:utf-8
import math

def g2kg(g):
    return g/1000.0

def getTriangleThirdSide(a,b):
    return math.sqrt(a**2+b**2)

if __name__ == "__main__":
    num=input ('please input a num')
    print (str(num)+'g = '+str(g2kg(num))+'kg')
    (side1,side2)=input ('please input 2 side length of a right triangle:')
    print ('the right triangle third side\'s length is '+str(getTriangleThirdSide(side1,side2)))


