from datetime import time

from pygame import Vector2

import core
from ceres.map import Map


class Projectiles:
    def __init__(self):
        self.map = Map()
        self.taille = 4
        self.vitesse = Vector2()
        self.acc = Vector2()
        self.vMax = 20
        self.aMax = 1
        self.position = Vector2()
        self.duréeDeVie = 4
        self.startTime = time.time()

    def draw(self):
        core.Draw.circle((240, 240, 240), self.position, self.taille)

    def move(self):
        self.vitesse += self.acc
        self.position += self.vitesse

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        if self.acc.length() > self.aMax:
            self.acc.scale_to_length(self.aMax)

    def shoot(self):
        if core.getMouseLeftClick():
            self.map.addprojectile()

        for a in self.map.projectile:
            if time.time() - a.startTime > a.duréeDeVie:
                self.map.projectile.remove(a)
                self.map.score -= 5

    def collision(self):
        pass

