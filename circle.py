from graphics import *
win=GraphWin("Circle",400,400)
win.setCoords(-200,-200,200,200)
def circle(xc,yc,r):
    
    x=0
    y=r
    d=(5/4)-r
    
    while(y>=x):
        draw(x,y,xc,yc)
        #print(x);print(y)
        #print(d)
        if(d<=0):
            d+=(2*x+3)
        else:
            y-=1
            d+=(2*(x-y)+5)
            
        x+=1
    #print(x);print(y)
    draw(x,y,xc,yc)
    
    win.getMouse()
    win.close()
def draw(x,y,xc,yc):
    
    Point(xc+x,yc+y).draw(win)
    Point(xc+y,yc+x).draw(win)
    Point(xc+y,yc-x).draw(win)
    Point(xc+x,yc-y).draw(win)
    
    Point(xc-x,yc+y).draw(win)
    Point(xc-y,yc+x).draw(win)
    Point(xc-y,yc-x).draw(win)
    Point(xc-x,yc-y).draw(win)
circle(int(input("enter xc:")),int(input("enter yc:")),int(input("enter radius:")))