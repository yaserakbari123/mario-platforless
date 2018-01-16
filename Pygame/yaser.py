import os
import random
import pygame
import sys
from pygame.locals import *
import math
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Super Mario Galaxy - Gusty Garden Galaxy.mp3")
pygame.mixer.music.play(loops=-1)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


display_width = 640
display_height = 480

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mario vs Microtransactions')



#background image
StartImg = pygame.image.load('Start.jpg')
menuImg = pygame.image.load('Mario Start Screen.jpg')
settingImg = pygame.image.load('Settings.jpg')
musicoffImg = pygame.image.load('Music off.jpg')
musiconImg = pygame.image.load('Music.jpg')
creditsImg = pygame.image.load('Credits.jpg')
creditspic = pygame.image.load('Creditspic.jpg')
creditsback = pygame.image.load('back.jpg')
ximage = 40; # x coordnate of image
yimage = 140; # y coordinate of image
ximage2 = 40; 
yimage2 = 240;
ximage3 = 40; 
yimage3 = 340;

gameDisplay.blit(StartImg ,  ( ximage,yimage)) # paint to screen
pygame.display.flip() # paint screen one time

def start():
    gameDisplay.blit(StartImg,(ximage, yimage))

def menu():
    gameDisplay.blit(menuImg,(0, 0))
   
def setting():
    gameDisplay.blit(settingImg,(40, 240))

def Credits():
    gameDisplay.blit(creditsImg,(40, 340))

def Creditspic():
    gameDisplay.blit(creditspic,(0, 0))

def Creditsback():
    gameDisplay.blit(creditsback,(0, 0))

def musicoff():
    gameDisplay.blit(musicoffImg,(10, 150))

def musicon():
    gameDisplay.blit(musiconImg,(260, 150))    

x = (display_width * 0.45)
y = (display_height * 0.8)

screen = 1

running = True

while (running):
    if screen == 1: #start menu
        menu()
        start()
        setting()
        Credits()
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if StartImg.get_rect().collidepoint(x-ximage, y-yimage):
                           
                    background = pygame.image.load('background.jpg')
                    died = pygame.image.load('You died.jpg')
                    died = pygame.transform.scale(died, (640,480))

                    dead = False

                    def gameover():
                        gameDisplay.blit(died,(0, 0))
                        pygame.display.update()

                    def back():
                        gameDisplay.blit(background,(0, 0))
                        pygame.display.update()
                     



                    UP='up'
                    LEFT='left'
                    RIGHT='right'
                    DOWN='down'

                    spritex = 300
                    spritey = 445
                    direction = None

                    pygame.draw.rect(gameDisplay, red, (300,449,30,30), 2)
                    pygame.display.update()
                    sprite = pygame.draw.rect(gameDisplay, red, (300,449,30,30), 2)

                    obstacleX = random.randint(40, 600)
                    obstacleY = 0

                    sprite=pygame.image.load('Left.png')
                    sprite=pygame.transform.scale(sprite, (35,35))
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
                        
                        gameDisplay.fill(white)
                        pygame.draw.circle(gameDisplay, blue, (obstacleX,obstacleY), 40, 1)#obstacle
                        #if marioRight:
                            #screen.blit(spriteR, (spritex, spritey))
                        #else:
                        gameDisplay.blit(sprite, (spritex, spritey))
                        #pygame.draw.rect(screen, red, (spritex,spritey,30,30), 2)
                        pygame.display.update()
                    else:
                        gameover()
                        pygame.display.update()
                        pygame.time.wait(1000)
                    #-------------

                elif settingImg.get_rect().collidepoint(x-ximage2, y-yimage2):
                   print('Settings')
                   screen = 3
                elif creditsImg.get_rect().collidepoint(x-ximage3, y-yimage3):
                   print('Credits')
                   screen = 4
  
    
    if screen == 3: #settings screen with back button
        menu()
        musicon()
        musicoff()
        Creditsback()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if creditsback.get_rect().collidepoint(x-0, y-0):
                   screen = 1
                elif musicoffImg.get_rect().collidepoint(x-10, y-150):
                   pygame.mixer.music.stop()
                elif musiconImg.get_rect().collidepoint(x-260, y-150):
                   pygame.mixer.music.stop()
                   pygame.mixer.music.load("NFL_Theme_Song_HQ[Mp3Converter.net].mp3")
                   pygame.mixer.music.play()



    elif screen == 4: #creditpic()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("NFL_Theme_Song_HQ[Mp3Converter.net].mp3")
        pygame.mixer.music.play()
        Creditspic()
        Creditsback()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if creditsback.get_rect().collidepoint(x-0, y-0):
                   print('menu screen')
                   screen = 1
  

    pygame.display.update()

             
    
    

