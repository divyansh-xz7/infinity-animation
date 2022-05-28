import pygame as pg
import random2 as rn

a=1000
b=600

d=pg.display.set_mode((a,b))

crashed=False

points=[]
point=0
shadows=[]
mode=0
s=0
np=len(points)
sc=0

while np<1:

    points.append([int(a/2),int(b/2),10000,5000,255,1])
    np=len(points)
    



while crashed==False:
    point=0
    shadow=0
    
    d.fill((0,0,0))

    for event in pg.event.get():

        if event.type==pg.QUIT:
            crashed=True

                   
    while shadow<len(shadows):
        sx=shadows[shadow][0]
        sy=shadows[shadow][1]
        sc=int((shadow)*1.25)
        pg.draw.circle(d,(0,0,sc),(int(sx),int(sy)),10)
        shadow+=1
        

    while point<1:

        x=points[point][0]
        y=points[point][1]
        xc=points[point][2]
        yc=points[point][3]
        c=points[point][4]
        i=points[point][5]

        ca=int(c)

        pg.draw.circle(d,(0,0,sc),(int(x),int(y)),10)

        
        ## mode selection
        if (xc==10000 or xc==-10000) and yc==5000:
            mode=0

        elif xc==10000 and yc==0:
            if mode==0:
                mode=1
            elif mode==5:
                mode=6
                i=1

        elif xc==-10000 and yc==0:
            if mode==0:
                mode=4
            if mode==2:
                mode=3
                i=-1

        elif xc==0 and yc==-10000:
            if mode==1:
                mode=2
            if mode==4:
                mode=5


        ### xc yc change

        if mode==0:
            if i==1:
                xc=10000
                local_xc=6000
            if i==-1:
                xc=-10000
                local_xc=-6000
            yc-=25

        elif mode==1:
            xc-=100
            yc-=100

        elif mode==2:
            xc-=100
            yc+=100

        elif mode==3:
            xc=-10000
            local_xc=-6000
            yc+=25

        elif mode==4:
            xc+=100
            yc-=100

        elif mode==5:
            xc+=100
            yc+=100

        elif mode==6:
            xc=10000
            local_xc=6000
            yc+=25

        ## x, y
        if mode==0 or mode==3 or mode==6:
            points[point][0]+=local_xc/10000
        else:
            points[point][0]+=xc/10000
        points[point][1]+=yc/10000



        points[point][2]=xc
        points[point][3]=yc
        points[point][4]=c
        points[point][5]=i

        s+=1
        if s==5:
            locala=points[0][0]
            localb=points[0][1]
            shadows.append([locala,localb])
            s=0
            
                
                
                
            
        

        

        point+=1


    
    pg.display.update()

        
    if len(shadows)>200:
        shadows.remove(shadows[0])
    

pg.quit()
quit()
