import pygame   #import pygame
pygame.init()    #initilize pygame
gray = (119,118,110)      #RGB color or Gray

#Display Width
display_width=600
display_height =800


gamedisplay = pygame.display.set_mode((display_width,display_height))

#display caption(title)
pygame.display.set_caption("car Game")
clock = pygame.time.Clock()

#define variable to load image from dir
carimg =pygame.image.load('car.jpg')

midimg=pygame.image.load('qq.jpg')

backgroungimg=pygame.image.load('stop.jpg')
 
car_width = 75

def background():
    gamedisplay.blit(backgroungimg,(0,0))
    gamedisplay.blit(midimg,(100,-1))
    
    gamedisplay.blit(backgroungimg,(500,0))
   
  

#define car  x,y position
def car(x,y):
    #blit is use to drage image from position to position
    gamedisplay.blit(carimg,(x,y))


def game_loop():
    #used for placeing draging object in screen. i.e object position on screen
    x =(display_width*0.5)
    y = (display_height*0.84)
    x_change=0


#basically used for exit event
    bumpad = False
    while not bumpad:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                bumpad=True


        #Keydown is basically used for control object from keys
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change =-5
            if event.key==pygame.K_RIGHT:
                x_change=5

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                    x_change=0

            x += x_change

        #calls the method
        gamedisplay.fill(gray)
        background()
        car(x,y)
        #
        if x>500-car_width or x<110:
            bumpad = True
            print('crashed')

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

