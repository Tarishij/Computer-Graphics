# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 19:07:58 2019

@author: PRIYANKA JAIN
"""
from graphics import *
win=GraphWin("ellipse",400,400)
win.setCoords(-200,-200,200,200)

def EllipsePoint(xc,yc,x,y):
    Point(xc+x,yc+y).draw(win)
    Point(xc+x,yc-y).draw(win)
    Point(xc-x,yc+y).draw(win)
    Point(xc-x,yc-y).draw(win)
    
def ellipse(xc,yc,a,b):
    
    x=0
    y=b
    d=b*b-a*a*b+0.25*a*a
    EllipsePoint(xc,yc,x,y)
    
    #region 1
    
    while(a*a*(y-0.5)>b*b*(x+1)):
        if(d<0):
            d+=(b*b*(2*x+3))
        else:
            d+=(b*b*(2*x+3)+a*a*(2-2*y))
            y-=1
        x+=1
        EllipsePoint(xc,yc,x,y)
    
    d2=b*b*(x+0.5)*(x+0.5)+a*a*(y-1)*(y-1)-a*a*b*b
    
    while(y>0):
        if(d2<0):
            d2+=(b*b*(2*x+2)+a*a*(3-2*y))
            x+=1
        else:
            d2+=a*a*(3-2*y)
        y-=1
        EllipsePoint(xc,yc,x,y)
    win.getMouse()
    win.close()
ellipse(int(input("enter xc:")),int(input("enter yc:")),int(input("enter a:")),int(input("enter b:")))