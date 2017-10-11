import turtle
import random
import math

Window = turtle.Screen()
pen = turtle.Pen()
pen.speed(0)
pen.penup()
pen.goto(0,-350)
pen.pendown()
pen.pensize(50)
pen.left(90)

brown = "#B69200"
green = "#00B63D"

x = raw_input("hit enter to start tree\n")

def Branch(p_size,length,depth): 
    if depth >= 7:
        pen.pencolor(green)
    else:
        pen.pencolor(brown)
        
    pen.pensize(p_size)
    pen.pendown()
    pen.forward(length)
    pen.penup()
    
    if depth < 8:
        tRot = random.randint(15,75)
        cRot = random.randint(-10,10)
        pen.left(tRot)
        Branch(math.floor(p_size*.75),math.floor(length*.67),depth+1)
        pen.backward(math.floor(length*.67))
        pen.right(tRot)
        
        if cRot > 0:
            pen.right(cRot)
            Branch(math.floor(p_size*.75),math.floor(length*.67),depth+1)
            pen.backward(math.floor(length*.67))
            pen.left(cRot)
            
        elif cRot < 0:
            pen.left(cRot)
            Branch(math.floor(p_size*.75),math.floor(length*.67),depth+1)
            pen.backward(math.floor(length*.67))
            pen.right(cRot)

        else:
            Branch(math.floor(p_size*.75),math.floor(length*.67),depth+1)
            pen.backward(math.floor(length*.67))

        pen.right(tRot)   
        Branch(math.floor(p_size*.67),math.floor(length*.67),depth+1)
        pen.backward(math.floor(length*.67))
        pen.left(tRot)

Branch(35,200,0) 
print "done"
        

        
