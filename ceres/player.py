import random
from pygame import Vector2

import core
from ceres.map import Map


class Player:
    def __init__(self):
        self.position = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.acc = Vector2(0,0)
        self.speed = Vector2(0,0)
        self.vMax = 5
        self.aMax = 2
        self.orientation = Vector2(0, -1)
        self.couleur = (240, 240, 240)
        self.taille = 12
        self.nbrVie = 3

    def show(self):
        p1 = self.orientation.rotate(90)
        p1.scale_to_length(10)
        p1 += self.position

        p3 = self.orientation.rotate(-90)
        p3.scale_to_length(10)
        p3 += self.position

        p2 = Vector2(self.orientation)
        p2.scale_to_length(20)
        p2 += self.position

        core.Draw.polygon(self.couleur, ((p1), (p2), (p3) ))

    def drawPlayer(self):
        core.Draw.circle((self.couleur), self.position,5)

    def movePlayer(self):
        if core.getKeyPressList("z"):
            self.acc= Vector2(self.orientation)
            self.speed += self.acc
            self.position +=self.orientation

        if core.getKeyPressList("d"):
            self.orientation = self.orientation.rotate(5)

        if core.getKeyPressList("q"):
            self.orientation = self.orientation.rotate(-5)


        self.position += self.acc
        self.acc = self.acc * 0.97

        if self.speed.length() > self.vMax:
            self.speed.scale_to_length(self.vMax)

        if self.acc.length() > self.aMax:
            self.acc.scale_to_length(self.aMax)


