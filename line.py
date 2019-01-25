from graphics import *
def line(x1,y1,x2,y2):
    win=GraphWin("my",400,400)
    win.setCoords(-200,-200,200,200)
   # Line(Point(x1,y1),Point(x2,y2)).draw(win)  #to check our line with actual line
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
  
    win.getMouse()
    win.close()  
line(int(input()),int(input()),int(input()),int(input()))
