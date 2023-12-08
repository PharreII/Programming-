from graphics import *
import math
winWH=600
win = GraphWin("patchwork", winWH, winWH)


def drawAlmond(x,y,w,h,color):
    count=10
    gap=h/count
    for i in range(count+1):
        ofs = i * gap
        line = Line(Point(x,y+ofs), Point(x+ofs,y+h))
        line.setOutline(color)
        line.draw(win)
        line = Line(Point(x+w,y+h-ofs), Point(x+h-ofs,y))
        line.setOutline(color)
        line.draw(win)

def drawCircle(centre,radius,color):
    shape = Circle(centre, radius)
    shape.setFill(color)
    shape.setOutline(color)
    shape.draw(win)

def drawRectangle(x,y,w,h,color):
    shape = Rectangle(Point(x,y), Point(x+w,y+h))
    shape.setFill(color)
    shape.setOutline(color)
    shape.draw(win)

def drawPill(x,y,w,h,color):
    radius = h/2
    drawCircle(Point(x+radius,y+radius),radius,color)
    drawRectangle(x+radius,y,w-(radius*2),h,color)
    drawCircle(Point(x+w-radius,y+radius),radius,color)

def drawPattern(x,y,w,h,color):
    WH = w/5
    circleRadius = WH/2
    pillW = 1.5*WH
    isCircle=True

    xOfs=0
    yOfs=0
    
    for row in range(0,5):
        for col in range(0,4):
            if isCircle:
                drawCircle(Point(x+xOfs+circleRadius,y+yOfs+circleRadius),circleRadius, color)
                xOfs=xOfs+WH
                isCircle=False
            else:
                drawPill(x+xOfs,y+yOfs,pillW,WH,color)
                xOfs=xOfs+pillW
                isCircle=True
        xOfs=0
        yOfs=yOfs+WH
        isCircle=not isCircle


#drawPattern(100,100,100,100,"black")
#drawPattern(0,0,100,100,"black")
#drawPattern(100,300,100,100,"black")

def draw(size,colors):
    w=h=winWH/size
    
    for y in range( 0, size):
        for x in range( 0, size):
            color = getColor(x,y,size, colors)
            type = getType(x,y,size)
            if type==' ':
                drawRectangle(x*w,y*h,w,h,color)
            elif type=='P':
                drawPattern(x*w,y*h,w,h,color)
            else:
                drawAlmond(x*w,y*h,w,h,color)

def getType(x,y,size):
    if y % 2 == 1:
        return ' '
    elif (x+y<size) and (x>0 and x<size-1) and (y>0 and y<size-1):
        return 'P'
    else:
        return 'F'

def getColor(x,y,size,colors):
    if x==0 or y==0: return colors[0]
    if x==size-1 or y==size-1: return colors[0]
    if x+y<size: 
        return colors[1]
    else:
        return colors[2]

def main():
    size=5
    colors=['Blue','orange','red']           
    if True:
        size = int(input("Enter the patchwork size (5, 7, 9 or Custom): "))
        colors = []
        for i in range(3):
            color = input(f"Enter color {i + 1}: ")
            colors.append(color)
            if color==0 or color==(size-1):
                return 0
    
    draw(size,colors)
main()
win.getMouse()


