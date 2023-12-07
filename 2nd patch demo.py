
from graphics import *

win = GraphWin("patchwork", 500, 500)

for i in range(11):
    w=100
    h=100
    x = (10 * i)
    y = (10 * i)
    line = Line(Point(0, y), Point(x, h))
    line.setOutline("red")
    line.draw(win)
    line = Line(Point(w, h-y), Point(w-x, 0))
    line.setOutline("red")
    line.draw(win)

win.getMouse()

