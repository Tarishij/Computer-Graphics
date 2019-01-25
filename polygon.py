# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:21:06 2019

@author: mnit
"""

from  graphics import *
win=GraphWin("my",400,400)
win.setCoords(-200,-200,200,200)
def line(x1,y1,x2,y2):
    
   # Line(Point(x1,y1),Point(x2,y2)).draw(win)
    a=abs(y2-y1)
    b=-abs(x2-x1)
    y=min(y1,y2)
    x=min(x1,x2)
    flag=0
    if(x1==x2):
        while(y<=max(y1,y2)):
            Point(x,y).draw(win)
            y+=1
            flag=1
    else:    
        m=(y2-y1)/(x2-x1)
    if(flag==0 and m>=0 and m<=1):
        
        d=2*a+b
        same=2*a
        add=2*(a+b)
        for x in range(min(x1,x2),max(x2,x1)+1):
            Point(x,y).draw(win)
            if(d>=0):
                y+=1
                d+=add
            else:
                d+=same
    elif (flag==0 and m>1):
        d=a+2*b
        add=2*(a+b)
        same=2*b
        for y in range(min(y1,y2),max(y1,y2)+1):
            Point(x,y).draw(win)
            if(d<=0):   
                x+=1
                d+=add
            else:
                d+=same
    elif(flag==0 and m<0 and m>-1):
        if(x1>x2 and y1<y2):
            t=x1
            x1=x2
            x2=t
            
            t=y1
            y1=y2
            y2=t
        
        a=(y2-y1)
        b=-(x2-x1)
        d=2*a-b
        add=2*(a-b)
        same=2*a
        y=max(y1,y2)
        while(x<=max(x1,x2)):
            Point(x,y).draw(win)
            if(d>=0):
                d+=same
               
            else:
                d+=add
                y-=1
            x+=1
    elif(flag==0 and m<=-1):
        if(x1>x2 and y1<y2):
            t=x1
            x1=x2
            x2=t
            
            t=y1
            y1=y2
            y2=t
        
        a=(y2-y1)
        b=-(x2-x1)
        d=a-2*b
        same=-2*b
        add=2*(a-b)
        y=max(y1,y2)
        while(x<=max(x1,x2)):
            Point(x,y).draw(win)
            if(d<=0):
                d+=same
            else:
                d+=add
                x+=1
            y-=1
  
   
def polygon(sides):
    
    x=[]
    y=[]
    for i in range(0,sides):
        print("enter coords")
        x.append(int(input("x coordinATE:")))
        y.append(int(input("y coordinate:")))
    for i in range(0,sides):
        if(i!=sides-1):
            line(x[i],y[i],x[i+1],y[i+1])
        else:
            line(x[i],y[i],x[0],y[0])
    win.getMouse()
    win.close() 
    
a=int(input("enter side of polygon"))
if(a<3):
    print("enter side greater than 2")
else:
    polygon(a)