import pygame
pygame.init()
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600
import time
import random


gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.jpg')
backgroundpic=pygame.image.load("download12.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("background.jpg")
instruction_background=pygame.image.load("background2.jpg")
car_width=56
pause=False

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is an car game in which you need dodge the coming cars",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_objects("A : ACCELERATOR",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((150),(550))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)


def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car1.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("car7.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))

def car(x,y):
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    fps=120

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
         
        clock.tick(60)

game_loop()
pygame.quit()
quit()
