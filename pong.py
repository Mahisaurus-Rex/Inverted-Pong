import pygame
import time
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1280,720))
done = False
#set initial variables
p1_x,p1_y=30,30
p2_x,p2_y=(screen.get_width()-60),30
ball_x,ball_y=((screen.get_width())/2),((screen.get_height())/2)
slope_x,slope_y=1.5,1.5
#set constants
paddle_width=screen.get_width()/64
paddle_height=screen.get_height()/3.6
#set initial conditions
p1_score,p2_score,paddle_score=0,0,0
p1=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p1_x,p1_y,paddle_width,paddle_height))
p2=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p2_x,p2_y,paddle_width,paddle_height))
ball=pygame.draw.rect(screen, (255,255,255), pygame.Rect(ball_x,ball_y,paddle_width,paddle_width))
#def checkScores():
#start program
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    #move paddles
    if pressed[pygame.K_w] and p1_y>0: 
        p1_y-=3
        p2_y-=3
    if pressed[pygame.K_s] and p1_y<screen.get_height()-200: 
        p1_y+=3
        p2_y+=3
    #make ball movement
    #ball control
    ball_x+=slope_x
    if pressed[pygame.K_UP] and ball_y>0: ball_y-=1.2
    if pressed[pygame.K_DOWN] and ball_y<screen.get_height()-paddle_width: ball_y+=1.2
    if ball_y <= 0 or ball_y >= (screen.get_height()):
        slope_y*=-1
    if ball_x <= 0:
        slope_x*=-1
        p2_score+=1
        ball_x,ball_y=((screen.get_width())/2),((screen.get_height())/2)
        time.sleep(1)
    if ball_x >= (screen.get_width()):
        slope_x*=-1
        p1_score+=1
        ball_x,ball_y=((screen.get_width())/2),((screen.get_height())/2)
        time.sleep(1)
    #collision
    if ball.colliderect(p1) or ball.colliderect(p2):
        if ball.colliderect(p2): slope_x=-1.5
        if ball.colliderect(p1): slope_x=1.5
        paddle_score+=1
        if slope_y>0:
            slope_y=random.randint(1,3) * -1
        else:
            slope_y=random.randint(1,3)
        ball_x+=(slope_x*4)
        ball_y+=slope_y
    #make players and ball
    screen.fill((0,0,0))
    score = myfont.render(str(str(int(paddle_score/3))+" "+str(p1_score+p2_score)), True, (255,255,255))
    screen.blit(score, ((screen.get_width()/2)-20,0))
    p1=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p1_x,p1_y,paddle_width,paddle_height))
    p2=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p2_x,p2_y,paddle_width,paddle_height))
    ball=pygame.draw.rect(screen, (255, 236, 160), pygame.Rect(ball_x,ball_y,paddle_width,paddle_width))

    pygame.display.flip()
