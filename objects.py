from pygame import *
from drawFunctions import *

class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.player = 0
        self.state = 0
        self.imagelist = ["images/player/Yellow Dino Standing.png", "images/player/Yellow Dino Walk.png", "images/player/Red Dino Standing.png", "images/player/Red Dino Walk.png", "images/player/Blue Dino Standing.png", "images/player/Blue Dino Walk.png"]
        self.processedImage = []
        for img in self.imagelist:
            self.processedImage.append(transform.scale(image.load(img), (125, 125)))
        self.mask = mask.from_surface(self.processedImage[0])
        self.rect = self.mask.get_rect(center = (100, 100))

    #def updateMask(self, x, y):
        #self.rect.center = x, y
        #self.mask = mask.from_surface(self.processedImage[0])

    def change(self, num):
        if num == 1:
            self.player = 0
        elif num == 2:
            self.player = 1
        else:
            self.player = 2
    
    def drawChar(self, surface):
        surface.fill((0, 0, 0, 0))
        walk = 0
        if self.state < 8:
            walk = 1
        #self.mask = mask.from_surface(self.processedImage[self.player * 2 + walk])
        surface.blit(self.processedImage[self.player * 2 + walk], (0, 0))
        return surface
    
    def updateState(self):
        self.state += 1
        self.state %= 16

class PlayerCollisions(sprite.Sprite):
    def __init__(self, tmpimg):
        super(PlayerCollisions, self).__init__()
        self.img = transform.scale(image.load(tmpimg), (125, 125))
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

class Ground(sprite.Sprite):
    def __init__(self, img):
        super(Ground, self).__init__()
        self.img = img
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

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
