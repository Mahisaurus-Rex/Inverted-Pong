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
slope_x,slope_y=2,2
#set constants
paddle_width=screen.get_width()/64
paddle_height=screen.get_height()/3.6
#set initial conditions
p1_score,p2_score=0,0
p1=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p1_x,p1_y,paddle_width,paddle_height))
p2=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p2_x,p2_y,paddle_width,paddle_height))
ball=pygame.draw.rect(screen, (255,255,255), pygame.Rect(ball_x,ball_y,paddle_width,paddle_width))
#start program
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed=pygame.key.get_pressed()
    #move paddles
    if (ball_y<p1_y) and p1_y>0: 
        p1_y-=1.85
        p2_y-=1.85
    if (ball_y>p1_y) and p1_y<screen.get_height()-200: 
        p1_y+=1.85
        p2_y+=1.85
    #make ball movement
    #ball control
    ball_x+=slope_x
    if pressed[pygame.K_w] and ball_y>0: ball_y-=2
    if pressed[pygame.K_s] and ball_y<screen.get_height()-200: ball_y+=2
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
        slope_x*=-1
        if slope_y>0:
            slope_y=random.randint(1,3) * -1
        else:
            slope_y=random.randint(1,3)
        ball_x+=(slope_x*3)
        ball_y+=slope_y
    #make players and ball
    screen.fill((0,0,0))
    score = myfont.render(str(p1_score+p2_score), True, (255,255,255))
    screen.blit(score, ((screen.get_width()/2)-20,0))
    p1=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p1_x,p1_y,paddle_width,paddle_height))
    p2=pygame.draw.rect(screen, (255,255,255), pygame.Rect(p2_x,p2_y,paddle_width,paddle_height))
    ball=pygame.draw.rect(screen, (255, 236, 160), pygame.Rect(ball_x,ball_y,paddle_width,paddle_width))

    pygame.display.flip()
