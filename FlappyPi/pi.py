import pygame as pg

class Pi(object):
    def __init__(self, x, y):
        self.x =  x
        self.y = y
        self.gravity = 1

    def show(self, screen):
        black = (0,0,0)
        centre = (self.x, self.y)
        pg.draw.circle(screen, black, centre , 20, 0)

    def applyForce(self):
        self.y += self.gravity

    def fly(self):
        if pg.key.get_pressed()[pg.K_SPACE]:
                self.y -= 2