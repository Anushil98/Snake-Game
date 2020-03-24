import random
import time
import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 5

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Snake')
x_init = 100  # head pixel value
y_init = 100
direction = 'R'
eaten = 1
apple_x=0
apple_y=0
pix_array = [(x_init, y_init), (x_init - 20, y_init), (x_init - 40, y_init)]
loop_life=1
Score=0
mul=1
hit=()
fontObj = pygame.font.SysFont('comicsansms.ttf',32)
def update_pix(pix_array, coordinates):
    global eaten
    l = len(pix_array)
    t = pix_array[0]
    last=pix_array[-1]
    for i in range(1, l):
        temp = pix_array[i]
        pix_array[i] = t
        t = temp
    pix_array[0] = coordinates
    if eaten==1:
        pix_array.append(last)

    return pix_array


def drawcircle(coordinates):
    global eaten,Score,fontObj
    newSurface = pygame.display.set_mode((400, 400))
    global pix_array
    if pix_array[0] != coordinates:
        pix_array = update_pix(pix_array, coordinates)
    for i in pix_array:
        pygame.draw.circle(newSurface, (0, 0, 255), i, 10)
    pygame.draw.circle(newSurface, (0, 255, 0), pix_array[0], 10)
    appleGenerator(newSurface)
    textSurfaceObj = fontObj.render('Score: {}'.format(Score), True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 350)
    newSurface.blit(textSurfaceObj,textRectObj)
    pygame.draw.line(newSurface,(255,255,255),(0,300),(400,300),10)
    return newSurface


def appleGenerator(Surface):
    global apple_y, apple_x, eaten,FPS,Score,mul, pix_array
    if eaten==1:
        x = random.randrange(20, 380, 20)
        y = random.randrange(20, 280, 20)
        while (x,y) in pix_array:
            x = random.randrange(20, 380, 20)
            y = random.randrange(20, 280, 20)
        apple_x = x
        apple_y = y
        FPS+=1
        if FPS>20:
            FPS=20
    eaten=0
    pygame.draw.circle(Surface, (255, 0, 0), (apple_x, apple_y), 10)
def showEnd(hit_point):
    global hit
    hit = hit_point
    global FPS,fpsClock,fontObj
    textSurfaceObj = fontObj.render('You Failed',True,(255,255,255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200,150)
    global DISPLAYSURF
    pygame.draw.circle(DISPLAYSURF,(255,255,255),hit_point,10)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    fpsClock.tick(FPS)
    global loop_life
    loop_life=0


def moveRight():
    global x_init, y_init, pix_array, direction
    if x_init + 20 == 400:
        x_init = 0

    if (x_init + 20, y_init) in pix_array:
        print("Collision")
        showEnd((x_init + 20, y_init))
    else:
        x_init += 20
        direction = 'R'


def moveLeft():
    global x_init, y_init, pix_array, direction
    if x_init - 20 <= 0:
        x_init = 380

    if (x_init - 20, y_init) in pix_array:
        print("Collision")
        showEnd((x_init - 20, y_init))
    else:
        x_init -= 20
        direction = 'L'


def moveUp():
    global x_init, y_init, pix_array, direction
    if y_init - 20 <= 0:
        y_init = 280

    if (x_init, y_init - 20) in pix_array:
        print("Collision")
        showEnd((x_init, y_init - 20))
    else:
        y_init -= 20
        direction = 'U'


def moveDown():
    global x_init, y_init, pix_array, direction
    if y_init + 20 >= 300:
        y_init = 0
    if (x_init, y_init + 20) in pix_array:
        print("Collision")
        showEnd((x_init, y_init + 20))
    else:
        y_init += 20
        direction = 'D'


DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
while True:
    if loop_life==0:
        showEnd(hit)
        time.sleep(3)
        break
    flag = 0
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.scancode == 77:
            if direction == 'L':
                continue
            moveRight()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
            flag = 1
        if event.type == KEYDOWN and event.scancode == 75:
            if direction == 'R':
                continue
            moveLeft()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
            flag = 1
        if event.type == KEYDOWN and event.scancode == 72:
            if direction == 'D':
                continue
            moveUp()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
            flag = 1
        if event.type == KEYDOWN and event.scancode == 80:
            if direction == 'U':
                continue
            moveDown()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
            flag = 1
        if event.type == QUIT:
            print("Exiting")
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
    if flag == 0:
        if direction == 'R':
            moveRight()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
        elif direction == 'L':
            moveLeft()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
        elif direction == 'U':
            moveUp()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
        elif direction == 'D':
            moveDown()
            if (x_init,y_init)==(apple_x,apple_y):
                eaten=1
                Score = Score + (8 * mul)
                mul += 1
                print('eaten')
            DISPLAYSURF.blit(drawcircle((x_init, y_init)), (0, 0))
        pygame.display.update()
        fpsClock.tick(FPS)
