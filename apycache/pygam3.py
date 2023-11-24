import pygame
pygame.init()
win=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('rectangle moves')

bg=pygame.image.load('bg.jpg')
char=pygame.image.load('kungfu.png')

x=50
y=440
width=40
height=60
vel=15

isjump=False
jumpcount=10

left=False
right=False

run=1
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT]and x<500-width-vel:
        x+=vel
    if not(isjump):       
        if keys[pygame.K_UP] and y>vel:    
            y-=vel
        if keys[pygame.K_DOWN]and y<500-height-vel:
            y+=vel
        if keys[pygame.K_SPACE]:
            isjump =True
    else:
        if jumpcount>=-10:
            neg=1
            if jumpcount<0:
                neg=-1
            y-=(jumpcount**2)*0.5*neg
            jumpcount-=1
        else:
            isjump=False
            jumpcount=10
                
    win.blit(bg,(0,0))
    win.blit(char,(x,y))
    pygame.display.update()
    
pygame.quit()            
