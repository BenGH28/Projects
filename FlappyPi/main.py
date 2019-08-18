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
from sys import exit

pg.init()
size = 400, 400
screen = pg.display.set_mode(size)
# pg.display.flip()
# running = True
# while running:
#     for event in pg.event.get():
#         if event == pg.QUIT:
#             running = False
#             pg.display.quit()
#             pg.quit()
# exit()
