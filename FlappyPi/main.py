"""
needed:
    flappyPi:
        object fixed in the x axis yet dynamic in the y.
        gravity to pull on the object 
        a floor/ceiling so that the object can't go off screen
    greek Pillars:
        obstacles sprouting from the floor and ceiling
        generated every ??? distance 
        random length 
        both meeting in the middle with just a large enough gap for flappyPi to fit
"""

import pygame as pg
import sys
from pygame.locals import *
from pi import Pi 

#the window to play in===========================================
pg.init()
height = 800
width = 400
size = (width, height)
gameWindow = pg.display.set_mode(size)
pg.display.set_caption("Flappy Pi")
pg.display.flip()

#the colours used================================================
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

#the Sprite======================================================
flappy = Pi(200,200)

#The Game Loop===================================================
while True:
    gameWindow.fill(WHITE)
    flappy.show(gameWindow)
    flappy.applyForce()  
    flappy.fly()

    if flappy.y >= height:
            pg.quit()
            sys.exit()
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
    pg.display.update()