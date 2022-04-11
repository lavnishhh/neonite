import random
import pygame
from pygame import *
pygame.init()
clock = pygame.time.Clock()
clock.tick(60)
f=0
font=pygame.font.SysFont('Arial',50)
a=10
b=10
c=10
win=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        #important variables#

                           
obstacle_speed=10
race_length=500

                        #variables
obs_max=obstacle_speed*2
bs=0
ys=0
blue_score_surface=font.render(str(bs),False,(0,255,255))
yellow_score_surface=font.render(str(ys),False,(255,255,0))

blue_score_surface_reset=font.render(str(bs),False,(0,0,0))
yellow_score_surface_rese=font.render(str(ys),False,(0,0,0))

                        #object draw init

game_run=True
x1=730
y1=455
x2=730
y2=455
recharge_xcord=730
recharge_ycord=445
yellow_cord=(x2,y2)
blue_cord=(x1,y1)
yellow_charge=0
blue_charge=0
obstacle_list_xcord=[]
obstacle_list_ycord=[]
pygame.key.set_repeat(50)
color_change=240
                           #animation#
for a in range (0,510):
    b=a/4
    pygame.draw.rect(win,(b,0,0),(recharge_xcord,recharge_ycord,36,18),2)
    pygame.display.flip()
for a in range (0,730):
    pygame.draw.circle(win,(255,0,0),(a,455),5)
    pygame.draw.rect(win,(255,0,0),(recharge_xcord,recharge_ycord,36,18),2)
    pygame.display.flip()
    win.fill((0,0,0))
for a in range(0,20):
    color_change-=12
    x1=x1+1
    x2=x2+1
    y1=y1-1
    y2=y2+1
    pygame.draw.circle(win,(color_change,255,255),(x1,y1),5)
    pygame.draw.circle(win,(255,255,color_change),(x2,y2),5)
    pygame.draw.rect(win,(255,0,0),(recharge_xcord,recharge_ycord,36,18),2)
    pygame.display.flip()
    win.fill((0,0,0))
upper_border=y1-5
lower_border=y2
p=733
q=0
for a in range (0,733):
    q+=1
    pygame.draw.rect(win,(200,0,0),(p-q,upper_border,q*2,4))
    pygame.draw.rect(win,(200,0,0),(p-q,lower_border,q*2,4))
    pygame.draw.circle(win,(0,255,255),(x1,y1),5)
    pygame.draw.circle(win,(255,255,0),(x2,y2),5)
    pygame.draw.rect(win,(255,0,0),(recharge_xcord,recharge_ycord,36,18),2)
    pygame.display.flip()
    pygame.draw.rect(win,(0,0,0),(0,upper_border,1466,4))
    pygame.draw.rect(win,(0,0,0),(0,lower_border,1466,4))
    upper_border=upper_border-0.32
    lower_border=lower_border+0.32
    q=q+1

pygame.draw.rect(win,(255,0,0),(121.5,150,306,20),2) #left-blue
pygame.draw.rect(win,(255,0,0),(988.5,150,306,20),2) #right-yellow


collision=False
direction_start=766
curr_dir_xcord=1
curr_dir_ycord=1
a1=476
b1=10
a2=10
b2=10
pi=3.14

                #object repulsion
y1def=0
y2def=0
def object_coll():
    global y1
    global y2
    global y1def
    global y2def
    oldy1=y1
    oldy2=y2
    if(x1-x2==0 and abs(y2-y1)<=20):
        collision=True
        if(s_press==True):
            y1def=-10
            y2def=30
        elif(w_press==True):
            y2def=30
            y1def=-10
        elif(d_press==True):
            y1def=-10
            y2def=30
        elif(u_press==True):
            y1def=-30
            y2def=10
        y1=y1+y1def
        y2=y2+y2def
        
            
    else:
        collision=False
                    #object draw init
a=0
b=0
c=0
upper_border=215
lower_border=710
def draw_obj():
    global y1
    global y2
    if(y2>700):
        y2=700
    if(y2<=220):
        y2=225
    if(y1>700):
        y1=700
    if(y1<=220):
        y1=225
    pygame.draw.rect(win,(a,b,c),(0,upper_border,1466,5))
    pygame.draw.rect(win,(b,c,a),(0,lower_border,1466,5))
    pygame.display.flip()
    pygame.draw.circle(win,(0,255,255),(x1,y1),5)
    pygame.draw.circle(win,(255,255,0),(x2,y2),5)
    pygame.draw.rect(win,(c,a,b),(recharge_xcord,recharge_ycord,36,18),2)
    pygame.display.flip()
    
def erase_obj():
    pygame.draw.circle(win,(0,0,0),(x1,y1),5)
    pygame.draw.circle(win,(0,0,0),(x2,y2),5)
    pygame.display.flip()

                    #pre-game init


obstacle_list_xcord=[]
obstacle_list_ycord=[]
                    #variables
blue_charge_change=False
yellow_charge_change=False
blue_charge1=(blue_charge)//0.5
yellow_charge1=(yellow_charge)//0.5
s_press=False
w_press=False
d_press=False
u_press=False
pygame.draw.circle(win,(255,255,color_change),(960,160),10)
pygame.draw.circle(win,(color_change,255,255),(456,160),10)
a_c=True
b_c=False
c_c=False
c_a=False
c_b=False
c_c1=False
i=0
blue_invincibility=False
yellow_invincibility=False
blue_collision=False
yellow_collision=False
x1_fwd_press=False
x2_fwd_press=False
fp=True
gp=True
                    #game start    
game_run=True
while game_run==True:

                    #recharge bars
    if(x1==750 and y1==455):
        blue_invincibility=True
        if(i%10==0):
            bs+=1
    else:
        blue_invincibility=False
    if(x2==750 and y2==455):
        if(i%10==0):
            ys+=1
        yellow_invincibility=True
    else:
        yellow_invincibility=False
    if(i==obs_max):
        if(blue_charge<100):
            blue_charge+=1
            blue_charge_change=True
        if(yellow_charge<100):
            yellow_charge+=1
            yellow_charge_change=True
                    #recharge bar display
    if(blue_charge_change==True):
        pygame.draw.rect(win,(0,255,0),(124.5,153,blue_charge*3,14))
        pygame.display.flip()
        pygame.draw.rect(win,(0,0,0),(126.5+(blue_charge*3),153,(100-blue_charge)*3,14))
    if(yellow_charge_change==True):
        pygame.draw.rect(win,(0,255,0),(991.5,153,yellow_charge*3,14))
        pygame.display.flip()
        pygame.draw.rect(win,(0,0,0),(991.5+(yellow_charge*3),153,(100-yellow_charge)*3,14))
                    #obstacles
    if(i%obstacle_speed==0):#obstacle production speed
        obstacle_add=int(random.randint(220,690))
        obstacle_list_ycord.append(obstacle_add)
        obstacle_list_xcord.append(1470)
        f=f+1
        bs+=1
        ys+=1
    if(i%5==0):#obstacle refresh speed
        blue_col_test=True
        yellow_col_test=True
        for obstacle_index in range (len(obstacle_list_xcord)):
            pygame.draw.rect(win,(0,0,0),(obstacle_list_xcord[obstacle_index],obstacle_list_ycord[obstacle_index],4,20))
            obstacle_list_xcord[obstacle_index]-=10
        for obstacle_index in range (len(obstacle_list_xcord)):
            if(obstacle_list_xcord[obstacle_index]<10):
                    obstacle_list_ycord.pop(obstacle_index)
                    obstacle_list_xcord.pop(obstacle_index)
                    break
            
        pygame.display.flip()
        for obstacle_index in range (len(obstacle_list_xcord)):            
            pygame.draw.rect(win,(a,c,b),(obstacle_list_xcord[obstacle_index],obstacle_list_ycord[obstacle_index],4,20))
            if(y2>=obstacle_list_ycord[obstacle_index] and y2<=obstacle_list_ycord[obstacle_index]+20 and x2==obstacle_list_xcord[obstacle_index] and yellow_invincibility==False):
                erase_obj()
                x2=x2-10
                yellow_collision=True
                yellow_col_test=False
                ys-=1
            else:
                if(yellow_col_test==True):
                    yellow_collision=False
            if(y1>=obstacle_list_ycord[obstacle_index] and y1<=obstacle_list_ycord[obstacle_index]+20 and x1==obstacle_list_xcord[obstacle_index] and blue_invincibility==False):
                erase_obj()
                x1=x1-10
                blue_collision=True
                blue_col_test=False
                bs-=1
            else:
                if(blue_col_test==True):
                    blue_collision=False
    
                    #movements
    for event in pygame.event.get():
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_ESCAPE):
                pygame.quit()
                game_run=False
                    #left player movement
            erase_obj()
            if(event.key==pygame.K_d and blue_collision==False):
                x1_fwd_press=True
            if(blue_charge>=2 and x1_fwd_press==True):
                x1+=10
                blue_charge-=2
                bs-=1
            if(event.key==pygame.K_s):
                s_press=True
                blue_collision=False
            object_coll()
            if(collision==False and s_press==True):
                y1=y1+10
            if(event.key==pygame.K_w):
                blue_collision=False
                w_press=True
            object_coll()
            if(collision==False and w_press==True):
                y1=y1-10
                        
                    #right player movement
            if(event.key==pygame.K_RIGHT and yellow_collision==False):
                x2_fwd_press=True
            if (yellow_charge>=2 and x2_fwd_press==True):
                x2+=10
                yellow_charge-=2
                ys-=1
            if(event.key==pygame.K_DOWN):
                yellow_collision=False
                d_press=True
            object_coll()
            if(collision==False and d_press==True):
                y2=y2+10

            elif(event.key==pygame.K_UP):
                yellow_collision=False
                u_press=True
            object_coll()
            if(collision==False and u_press==True):
                y2=y2-10
        erase_obj()
        draw_obj()
        if(event.type==KEYUP):
                        #left player movement
            if(event.key==pygame.K_d):
                blue_boost=False
                x1_fwd_press=False
            if(event.key==pygame.K_s):
                s_press=False
                
            elif(event.key==pygame.K_w):
                w_press=False
                
                    #right player movement
            if(event.key==pygame.K_RIGHT):
                yellow_boost=False
                x2_fwd_press=False
            elif(event.key==pygame.K_DOWN):
                d_press=False
                
            elif(event.key==pygame.K_UP):
                u_press=False
                    #color
    if(a_c==True):
        if(a==254):
            a_c=False
            b_c=True
        a=a+1
    if(b_c==True):
        if(b==254):
            b_c=False
            c_c=True
        b=b+1
    if(c_c==True):
        if(c==254):
            c_a=True
            c_c=False
        c=c+1
    if(c_a==True):
        if(a==100):
            c_a=False
            c_b=True
        a=a-1
    if(c_b==True):
        if(b==1):
            c_b=False
            c_c1=True
        b=b-1
    if(c_c1==True):
        if(c==1):
            a_c=True
            c_c1=False
        c=c-1
                            #score
    if(ys<0):
        ys=0
    if(bs<0):
        bs=0
    blue_score_surface=font.render(str(bs),False,(0,255,255))
    yellow_score_surface=font.render(str(ys),False,(255,255,0))
    
    pygame.draw.rect(win,(0,0,0),(124.5,40,1160,70))
    win.blit(blue_score_surface,(124.5,40))
    win.blit(yellow_score_surface,(1191.5,40))
    pygame.display.update()
    if(f==race_length):
            
        if(bs>ys):
            print("left wins")
        else:
            print("right wins")
        game_run=False
        pygame.quit()
    if i==obs_max:
        i=0
    i=i+1
    draw_obj()