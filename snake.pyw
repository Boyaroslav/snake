import pygame

import random

pygame.init()
icon=pygame.image.load("icon.png")
font=pygame.font.Font("Connec.otf",30)
imj=pygame.image.load("apple2.png")
player=pygame.image.load("snakeblock.png")
bg=pygame.image.load("bg.png")
body=pygame.image.load("body.png")
head=pygame.image.load("head.png")
head2=pygame.image.load("headopen.png")
pygame.display.set_caption("snake")
timerofopen=2
eat=pygame.mixer.Sound("MMM.hd.mp3")
isopen=0
game=0
bestscore = []
root=pygame.display.set_mode((850,750))
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
foodx=random.randrange(0,560,20)
foody=random.randrange(0,560,20)
food=1
x=[240]
y=[240]
nap="right"
true=True
while true:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.KEYDOWN:
            if game==0:
                game=1
            if i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                if nap != "left":
                    nap = "right"
            if i.key == pygame.K_LEFT or i.key == pygame.K_a:
                if nap != "right":
                    nap = "left"
            if i.key == pygame.K_UP or i.key == pygame.K_w:
                if nap != "down":
                    nap = "up"
            if i.key == pygame.K_DOWN or i.key == pygame.K_s:
                if nap != "up":
                    nap = "down"

    root.blit(bg,(0,0))
    if game==0:
        bestscore.append(food)
        foodx = random.randrange(0, 560, 20)
        foody = random.randrange(0, 560, 20)
        food = 1
        x = [240]
        y = [240]
        nap = "right"
        pygame.draw.rect(root,(0,0,0),(200,300,450,250))
        text = font.render("press any button to start", True, (255, 255, 255))
        root.blit(text, (223, 415))
        tet="your best record is"+str(max(bestscore))
        text2=font.render(tet,True,(255,255,255))
        root.blit(text2,(275,500))

    if game:
        if foodx==x[0] and foody==y[0]:
            isopen=1
            timerofopen=2
            x.append(-10)
            y.append(-10)
            foodx = random.randrange(0, 560, 20)
            foody = random.randrange(0, 560, 20)
            food+=1
            eat.play()
            print(food)
        for i in range(len(x) - 1, 0, -1):
            x[i] = x[i - 1]
            y[i] = y[i - 1]
        if nap == "right":
            x[0] += 20
        if nap == "left":
            x[0] -= 20
        if nap == "up":
            y[0] -= 20
        if nap == "down":
            y[0] += 20
        for i in range(1,food):
            if foodx==x[i] and foody==y[i] and foody!=y[0] and foodx!=x[0]:
                foodx=random.randrange(0,560,20)
                foody=random.randrange(0,560,20)
            if x[0]==x[i] and y[0]==y[i]:
                game = 0
        root.blit(imj,(foodx,foody))
        for i in range(len(x)):
            root.blit(body,(x[i],y[i]))
        root.blit(head,(x[0],y[0]))
        if isopen:
            timerofopen-=1
            if timerofopen==0:
                isopen=0
            root.blit(head2, (x[0]-5, y[0]-5))
        score=str(food)+" score"
        text=font.render(score,True,(0,0,0))
        root.blit(text,(10,10))
        if x[0]<=-10:
            game=0
        if x[0]>=860:
            game=0
        if y[0]<=-10:
            game=0
        if y[0]>=760:
            game=0
    pygame.display.flip()
    clock.tick(20)
