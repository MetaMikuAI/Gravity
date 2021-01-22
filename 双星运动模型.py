import os
import sys
import math
import pygame
from cmath import *
from pygame.locals import *

N=10000;#记录点
G=1;#万有引力常数
global t;
global x;
global m;
global v;
x=[(0,0),(10,0)];
m=[100,1];
v=[(0,0),(0,2)];
dt=0.01;
t=0;
ArrayPa=[]
ArrayPb=[]
x_=x;

#显示
pygame.init();#显示初始化
size = width,height = 1600,1000 ;#显示屏大小(单位：px像素)
ZOOM = 0.02; #分辨率(模拟长度m/实际长度px)
FPS = 600;#帧率
screen = pygame.display.set_mode(size); #设置屏幕窗口
clock = pygame.time.Clock();#对接时钟
p_=(size[0]//2,size[1]//2);
COLOR=[(0,0,0),(255,0,0)];
BackColor=(255,255,255);
global p;
p=[(x[0][0]/ZOOM+p_[0],x[0][1]/ZOOM+p_[1]),(x[1][0]/ZOOM+p_[0],x[1][1]/ZOOM+p_[1])];
global ifmouse
ifmouse=0;
mouse_pos=p_;

def Array_init():
    for i in range(0,N):
        ArrayPa.append(p[0]);
        ArrayPb.append(p[1]);

Array_init();
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False;
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ifmouse=1;
        elif event.type == pygame.MOUSEBUTTONUP:
            ifmouse=0;
            
    r=math.sqrt((x[1][0]-x[0][0])*(x[1][0]-x[0][0])+(x[1][1]-x[0][1])*(x[1][1]-x[0][1]));
    F=G*m[0]*m[1]/(r*r);
    a_0x=F*(x[1][0]-x[0][0])/r/m[0];
    a_0y=F*(x[1][1]-x[0][1])/r/m[0];
    a_1x=F*(x[0][0]-x[1][0])/r/m[1];
    a_1y=F*(x[0][1]-x[1][1])/r/m[1];
    t+=dt;
    v=[(v[0][0]-a_0x*dt,v[0][1]-a_0y*dt),(v[1][0]-a_1x*dt,v[1][1]-a_1y*dt)];
    x=[(x[0][0]-v[0][0]*dt,x[0][1]-v[0][1]*dt),(x[1][0]-v[1][0]*dt,x[1][1]-v[1][1]*dt)];
    p=[(x[0][0]/ZOOM+p_[0],x[0][1]/ZOOM+p_[1]),(x[1][0]/ZOOM+p_[0],x[1][1]/ZOOM+p_[1])];
    
    
    if ifmouse==1:
        p=[(p[0][0],p[0][1]),pygame.mouse.get_pos()];
        x=[(x[0][0],x[0][1]),((p[1][0]-p_[0])*ZOOM,(p[1][1]-p_[1])*ZOOM)];
        v=[(v[0][0],v[0][1]),((x_[1][0]-x[1][0])/dt,(x_[1][1]-x[1][1])/dt)]
        mouse_pos=pygame.mouse.get_pos();
        x_=x;
        print (mouse_pos);
        
    
    ArrayPa.append(p[0]);
    ArrayPb.append(p[1]);
    ArrayPa.pop(0);
    ArrayPb.pop(0);
    
    screen.fill(BackColor);
    pygame.draw.circle(screen,COLOR[0],p[0],10);
    pygame.draw.circle(screen,COLOR[1],p[1],10);
    pygame.draw.lines(screen,COLOR[0],0,ArrayPa,3);
    pygame.draw.lines(screen,COLOR[1],0,ArrayPb,3);
    pygame.display.flip();
    pygame.display.set_caption("双星运动模型:t="+str(round(t,N)));#窗口标题
    clock.tick(FPS);
