import pygame
import sys
import random
from pygame.locals import *
import math

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("OWEN YASER and ANDREW GAME")



died = pygame.image.load('You died.jpg')
died = pygame.transform.scale(died, (640,480))

dead = False

def gameover():
    screen.blit(died,(0, 0))
    pygame.display.update()

UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

spritex = 300
spritey = 445
direction = None

pygame.draw.rect(screen, red, (300,449,30,30), 2)
pygame.display.update()
sprite = pygame.draw.rect(screen, red, (300,449,30,30), 2)

obstacleX = random.randint(40, 600)
obstacleY = 0

sprite=pygame.image.load('Left.png')
sprite=pygame.transform.scale(sprite, (30,30))
#spriteR=pygame.transform.flip(spriteL, True, False)
marioRight = True
marioLeft = False

def move(direction, spritex, spritey):
    if direction:
        if direction == K_LEFT:
            spritex -=0.75
            if spritex < 2 :
                spritex = 610
            marioLeft = True
            marioRight = False
            #print('left')
            
            #screen.blit(spriteL,(spritex, spritey))
        elif direction == K_RIGHT:
            spritex +=0.75
            if spritex > 620:
                spritex = 5
            marioRight = True
            marioLeft = False
            #print('right')
            #sprite=pygame.image.load('right.png')
    return spritex, spritey

while dead == False:
    
    dist = math.sqrt((spritex-obstacleX)**2 + (spritey-obstacleY)**2)

    if dist < 40 :
        dead = True

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if (event.key == direction):
                direction = None
    spritex, spritey = move(direction, spritex, spritey)
    obstacleY += 1

    if obstacleY > 600:
        obstacleX = random.randint(40, 600)
        obstacleY = -100
    
    screen.fill(white)
    pygame.draw.circle(screen, blue, (obstacleX,obstacleY), 40, 1)#obstacle
    #if marioRight:
        #screen.blit(spriteR, (spritex, spritey))
    #else:
    screen.blit(sprite, (spritex, spritey))
    #pygame.draw.rect(screen, red, (spritex,spritey,30,30), 2)
    pygame.display.update()
else:
    gameover()
    pygame.display.update()
#-------------
