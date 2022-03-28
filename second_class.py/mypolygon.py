from codecs import BOM_BE
from operator import length_hint
import turtle
bob = turtle.Turtle()
# print(bob)
# def square(t,length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
# square(bob,200)
# turtle.mainloop()

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        angle = 360/n
        t.lt(angle)
polygon(bob,100,8)

# import math
# def circle(t, r):
#         circum= 2*math.pi*r
#         n= int(circum/10)+1
#         length= circum/n
#         polygon(t,length, n)

# circle(bob, 100)
# bob.end_fill()
# turtle.done()
