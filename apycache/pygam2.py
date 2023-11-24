import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('rectangle moves')

x=50
y=440
width=40
height=60
vel=15

isjump=False
jumpcount=10

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
            y-=(jumpcount**2)*1*neg
            jumpcount-=1
        else:
            isjump=False
            jumpcount=10
                
    win.fill((0,0,0))
    pygame.draw.circle(win,(255,255,0),(x,y),50,0)
    pygame.display.update()
    
pygame.quit()            
