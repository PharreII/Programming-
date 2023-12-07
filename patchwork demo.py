from graphics import *

win = GraphWin("patchwork", 500, 500)


def circle(centre,radius):
    circle = Circle(centre, radius)
    circle.setFill("red")
    circle.setOutline("red")
    circle.draw(win)

def pill(centre,radius): 
    w=radius/2
    C = Circle(Point( centre.x-w,centre.y ), radius)
    C.setFill("red")
    C.setOutline("red")
    C.draw(win)

    R = Rectangle(Point(centre.x-w,centre.y-radius), Point(centre.x+w,centre.y+radius))
    R.draw(win)
    R.setFill("red")
    R.setOutline("red")

    C = Circle(Point( centre.x+w,centre.y ), radius)
    C.setFill("red")
    C.setOutline("red")
    C.draw(win)

def drawShapes(shapeXY):
    drawCircle=True
    circleW=20
    pillW=30
    shapeH=20

    for y in range(0,5):
        for x in range(0,4):
            if drawCircle:
                circle(shapeXY,10)
                shapeXY.x=shapeXY.x+circleW
                drawCircle=False
            else:
                pill(shapeXY,10)
                shapeXY.x=shapeXY.x+pillW
                drawCircle=True
        drawCircle=not drawCircle
        shapeXY.x=0
        shapeXY.y=shapeXY.y+shapeH
        
drawShapes(Point(0,0)) 

drawShapes(Point(100,100)) 
drawShapes(Point(160,100)) 

win.setBackground("white")
win.getMouse()




def main():
    
    size = int(input("Enter the patchwork size (5, 7, or 9): "))
    
    
    colors = []
    for i in range(3):
        color = input(f"Enter color {i + 1}: ")
        colors.append(color)

    
    draw_patchwork(size, colors)


if __name__ == "__main__":
    main()




def Drawpatch():
    drawpatch = true

    for p in range():
        if drawpatch