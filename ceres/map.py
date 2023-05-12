import time

from pygame import Vector2

import core


class Map:
    def __init__(self):
        self.init_done = False
        self.score = 0
        self.ast_detruit = 0
        self.maxplayer = 1
        self.maxasteroid = 10
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueur = None
        self.asteroid = []
        self.projectile = []
        self.starttime = time.time()


