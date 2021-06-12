import random
from numpy.core.arrayprint import format_float_scientific
import pygame
import numpy as np
import math

class Body:
    name=0
    pos=np.array([0,0])
    radius=0
    vel=np.array([0,0])
    direction=0
    mass=0
    force=np.array([0.0,0.0])
    acceleration=np.array([0.0,0.0])
    def __init__(self,name,pos,radius,vel,direction,mass):
        self.name=name
        self.pos=pos
        self.radius=radius
        self.vel=vel
        self.direction=direction
        self.mass=mass
        return
    def clear(self):
        name=0
        pos=np.array([0,0])
        radius=0
        vel=np.array([0,0])
        direction=0
        mass=0
        force=np.array([0.0,0.0])
        acceleration=np.array([0.0,0.0])
    
def bodyLnilist(self):
        input('place mouse')
        '''bool=True
        while bool:
            for event in pygame.event.get():
                print(event)
                if event.type==pygame.MOUSEMOTION:
                    pos=event.pos
                    print(pos)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    bool=False
                    continue


            clock.tick(15)'''
            

        radius=input('radius')
        
def move(bodies):
    #set vel
    BIG_G=.002
    
    for b1 in bodies:
        forces=np.array([0,0])
        for b2 in bodies:
            delx=b2.pos[0]-b1.pos[0]
            dely=b2.pos[1]-b1.pos[1]
            d=math.sqrt(delx**2+dely**2)        
            if d>5:
                if delx>0:
                    xsign=1
                else:
                    xsign=-1
                if dely>0:
                    ysign=1
                else:
                    ysign=-1
                
                force=np.array([0,0])
                netforce=BIG_G*b1.mass*b2.mass/(d**2)
                force[0]=xsign*netforce*math.sqrt(d**2-dely**2)
                force[1]=ysign*netforce*math.sqrt(d**2-delx**2)
                forces+=force
                if d<(b1.radius+b2.radius):
                    collide(b1,b2)

        b1.force=forces
        b1.acceleration=b1.force/b1.mass
        b1.vel+=b1.acceleration
    for b1 in bodies:
        b1.pos+=b1.vel
        
       # print('name:',b1.name,'vel:',mag(b1.vel))


def collide(b1,b2):
    newv1=b1.vel-2*b2.mass/(b1.mass+b2.mass)*np.dot(b1.vel-b2.vel,b1.pos-b2.pos)/mag(b1.pos-b2.pos)**2*(b1.pos-b2.pos)
    newv2=b2.vel-2*b1.mass/(b2.mass+b1.mass)*np.dot(b2.vel-b1.vel,b2.pos-b1.pos)/mag(b2.pos-b1.pos)**2*(b2.pos-b1.pos)
    b1.vel=newv1
    b2.vel=newv2
    b1.pos+=b1.vel
    b2.pos+=b2.vel
    return

def mag(x): 
    return math.sqrt(sum(i**2 for i in x))



def draw(disp,bodies,bodyset,newbody,mousepos):
    white=(255,255,230)
    green =(0,255,0)
    red = (255,0,50)
    darkred=(230,0,50)
    
    for i in bodies:
        pygame.draw.circle(disp, red, i.pos, i.radius, width=0)
    if bodyset>0:
        pygame.draw.circle(disp, darkred, newbody.pos, newbody.radius, width=0)
        if bodyset==3:
            pygame.draw.line(disp, (0,0,0), newbody.pos,mousepos, width=7)

    pygame.display.update()



def distance(a,b):
    delx=b[0]-a[0]
    dely=b[1]-a[1]
    
    d=math.sqrt(delx**2+dely**2)
    return d
def follow(bodies,b1):
    shift=[800,600]-bodies[b1].pos
    for i in bodies:
        i.pos+=shift
    return
    

 
def main():
    pygame.init()
    disp=pygame.display.set_mode((1600,1200))
    pygame.display.set_caption('coolgame001')
    clock= pygame.time.Clock()
    
    
    #bodyList=BodyList()
    mousepressed=False
    mousepos=(0,0)
    bodyList=[]
    nbindex=-1
    setvelconstant=.1

    bodyset=True
    followbool=False
    vailidInp=['0','1','2','3','4','5','6','7','8','9']
    follownumber=-1
    setstep=0
    
    while True:
        for event in pygame.event.get():
            
            #print(event)
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.scancode==41):
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                print(event)
                if event.scancode<=82 and event.scancode>=79:
                    print(event.scancode)
                if event.unicode=='p':  #play bool
                    
                    if play:
                        play=False
                        print('paused')
                    else:
                        print('play')
                        play=True
                if event.unicode=='n':  #new body
                    
                    if bodyset:
                        bodyset=False
                        setstep=0
                        bodyList.pop(nbindex)
                        nbindex-=1
                        print('creation cancelled')
                    else:
                        bodyset=True
                        print('create body')
                if event.unicode=='f':  #followbool
                    if followbool:
                        followbool=False
                        print('follow mode off')
                    else:
                        followbool=True
                        print('press number to follow body')
                if event.scancode==42:
                    bodyList.pop(nbindex)
                    nbindex-=1
    
                if followbool:
                    if vailidInp.count(event.unicode)==1 and int(event.unicode)<len(bodyList):
                        follownumber=int(event.unicode)
                        print(follownumber)
                    
                   
            if event.type==pygame.MOUSEMOTION:
                    mousepos=event.pos
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousepressed=True
            if event.type==pygame.MOUSEBUTTONUP:
                mousepressed=False
        if bodyset or (len(bodyList)==0): #bodyset fx
                bodyset=True
            
                if setstep==0:
                    play=False
                    nbindex+=1
                    bodyList.append(Body(nbindex,[100,100],20,[0,0],[0,0],10))
                    setstep=1
                if setstep==1:    
                    bodyList[nbindex].pos[0]=mousepos[0]
                    bodyList[nbindex].pos[1]=mousepos[1]
                    #print(bodyList[nbindex].pos)
                    if mousepressed:
                        setstep=2
                        mousepressed=False
                elif setstep==2:
                    bodyList[nbindex].radius=distance(bodyList[nbindex].pos,mousepos)
                    if mousepressed:
                        bodyList[nbindex].mass=bodyList[nbindex].radius**3
                        setstep=3
                        mousepressed=False
                elif setstep==3:
                    bodyList[nbindex].direction=[bodyList[nbindex].pos,mousepos]
                    #pygame.draw.line(disp, (0,0,0), bodyList[nbindex].pos,mousepos, width=7)
                    if mousepressed:
                        bodyList[nbindex].vel=setvelconstant*(np.array(mousepos)-np.array(bodyList[nbindex].pos))
                        if followbool and follownumber!=-1:
                            bodyList[nbindex].vel+=bodyList[follownumber].vel
                        mousepressed=False
                        bodyset=False
                        setstep=0
                        play=True
        

        #if velreset:
            #Velreset()
        if followbool and follownumber!=-1:
            follow(bodyList,follownumber)
        if play:
            move(bodyList) 
             
        disp.fill((125,125,125))
        
        
        draw(disp,bodyList,setstep,bodyList[nbindex],mousepos)
        
        
        clock.tick(90)
if __name__ == "__main__":

    main()