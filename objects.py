from pygame import *
#from drawFunctions import *

class Player(sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.player = 0
        self.state = 0
        self.orientation = 0
        self.scaling = 0
        self.imagelist = ["images/player/Yellow Dino Standing.png", "images/player/Yellow Dino Walk.png", "images/player/Red Dino Standing.png", "images/player/Red Dino Walk.png", "images/player/Blue Dino Standing.png", "images/player/Blue Dino Walk.png"]
        self.processedImage = []
        for img in self.imagelist:
            self.processedImage.append(transform.scale(image.load(img), (125, 125)))
        self.mask = mask.from_surface(self.processedImage[0])
        self.rect = self.mask.get_rect()

    def drawChar(self, surface):
        surface.fill((0, 0, 0, 0))
        walk = 0
        if self.state < 8:
            walk = 1
        output = self.processedImage[self.player * 2 + walk]
        if self.orientation:
            output = transform.flip(output, True, False)
        if self.scaling == 1:
            output = transform.rotate(output, 270)
        if self.scaling == 2:
            output = transform.rotate(output, 90)
        surface.blit(output, (0, 0))
        return surface
    
    def updateState(self):
        self.state += 1
        self.state %= 16
    
    def setOrientation(self, num):
        self.orientation = num

    def change(self, num):
        self.player = num - 1

    def setScaling(self, num):
        self.scaling = num

class PlayerCollisions(sprite.Sprite):
    def __init__(self, tmpimg):
        super(PlayerCollisions, self).__init__()
        self.img = transform.scale(image.load(tmpimg), (125, 125))
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

class Background(sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

class Ground(sprite.Sprite):
    def __init__(self, img):
        super(Ground, self).__init__()
        self.img = img
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

class Obstacle(sprite.Sprite):
    def __init__(self, img):
        super(Obstacle, self).__init__()
        self.img = img
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

class Trash(sprite.Sprite):
    def __init__(self, tmpimg, pos):
        super(Trash, self).__init__()
        self.x, self.y = pos
        self.collected = False
        self.img = tmpimg
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

class TrashLayer(sprite.Sprite):
    def __init__(self, img):
        super(TrashLayer, self).__init__()
        self.img = img
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

    def update(self, img):
        self.img = img
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()
    
class Button(sprite.Sprite):
    def __init__(self):
        super(Button, self).__init__()
        self.img = transform.scale(image.load("images/buttons/Play Button Normal State.png"), (125, 125)).convert_alpha()
        self.hoverimg = transform.scale(image.load("images/buttons/Play Button Hover State.png"), (125, 125)).convert_alpha()
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()

class Mouse(sprite.Sprite):
    def __init__(self):
        super(Mouse, self).__init__()
        self.surf = Surface((10, 10)).convert_alpha()
        self.surf.fill((0, 0, 0, 0))
        draw.rect(self.surf, "#FFFFFF", Rect(0, 0, 10, 10))
        self.mask = mask.from_surface(self.surf)
        self.rect = self.mask.get_rect()
        
class Treasure(sprite.Sprite):
    def __init__(self):
        super(Treasure, self).__init__()
        self.img = transform.scale(image.load("images/Treasure.png"), (125, 125)).convert_alpha()
        self.mask = mask.from_surface(self.img)
        self.rect = self.mask.get_rect()