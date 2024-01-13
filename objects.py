from pygame import *
from drawFunctions import *

class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.player = 1

    def change(self, num):
        if num == 1:
            self.player = 1
        elif num == 2:
            self.player = 2
        else:
            self.player = 3

class Ground(sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()

class Background(sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

class Obstacle(sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()

class Trash(sprite.Sprite):
    def __init__(self):
        super(Trash, self).__init__()

class Water(sprite.Sprite):
    def __init__(self):
        super(Water, self).__init__()
