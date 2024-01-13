from pygame import *
from drawFunctions import *

class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.player = 1
        self.state = 0
        self.imagelist = [transform.scale(image.load("images/Yellow Dino Standing.png"), (100, 100))]

    def change(self, num):
        if num == 1:
            self.player = 1
        elif num == 2:
            self.player = 2
        else:
            self.player = 3
    
    def drawChar(self, surface):
        surface.fill((0, 0, 0, 0))
        if self.player == 1 and self.state < 8:
            surface.blit(transform.scale(image.load("images/Yellow Dino Standing.png"), (125, 125)), (0, 0))
        else:
            surface.blit(transform.scale(image.load("images/Yellow Dino Walk.png"), (125, 125)), (0, 0))
        return surface
    
    def updateState(self):
        self.state += 1
        self.state %= 16

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
