from pygame import *
from objects import *

#WHITE = "#FFFFFF"

def drawTrashCollection(surface, trashList):
    surface.fill("#FFFFFF")
    width = surface.get_width
    height = surface.get_height

    #back and forward buttons
    draw.rect(surface, "#000000", Rect(0, 0, 100, 100))
    #draw.rect(surface, "#000000", Rect(0, 0, 100, 100))
    return surface

#loading all the grass blocks
grass1 = transform.scale(image.load("images/blocks/grass block 1.png"), (125, 125))
grass2 = transform.scale(image.load("images/blocks/grass block 2.png"), (125, 125))
grass3 = transform.scale(image.load("images/blocks/grass block 3.png"), (125, 125))
grass4 = transform.scale(image.load("images/blocks/grass block 4.png"), (125, 125))
grass5 = transform.scale(image.load("images/blocks/grass block 5.png"), (125, 125))
grass6 = transform.scale(image.load("images/blocks/grass block 6.png"), (125, 125))
grass7 = transform.scale(image.load("images/blocks/grass block 7.png"), (125, 125))
grass8 = transform.scale(image.load("images/blocks/grass block 8.png"), (125, 125))
grass0 = transform.scale(image.load("images/blocks/grass block 9.png"), (125, 125))
grassFloat = transform.scale(image.load("images/blocks/grass block float.png"), (125, 125))

def drawLevel1(surface):
    surface.fill((0, 0, 0, 0))
    # draw ground
    for i in range(0, 50):
        surface.blit(grass2, (i * 125, 800))
    # floating bit
    for i in range(0,3):
        surface.blit(grassFloat, (500 + (i * 125), 500))
    # small vertical
    surface.blit(grass2, (1300, 800 - 125))
    # medium vertical
    surface.blit(grass5, (1800, 800 - 125))
    surface.blit(grass2, (1800, 800 - (125 * 2)))
    # small vert
    surface.blit(grass3, (1800 + 125, 800 - 125))
    # large vertical ground
    surface.blit(grass4, (2500, 800 - 125))
    surface.blit(grass4, (2500, 800 - (125 * 2)))
    surface.blit(grass1, (2500, 800 - (125 * 3)))
    # highground
    for i in range (0,5):
        surface.blit(grass5, (2500 + 125 + (i * 125), 800 - 125))
        surface.blit(grass5, (2500 + 125 + (i * 125), 800 - (125 * 2)))
        surface.blit(grass2, (2500 + 125 + (i * 125), 800 - (125 * 3)))
    # high floating blocks
    surface.blit(grassFloat, (2500 + (125 * 7), 800 - (125 * 5)))
    surface.blit(grassFloat, (2500 + (125 * 8), 800 - (125 * 5)))
    # slightly high ground
    for i in range (0,3):
        surface.blit(grass5, (2500 + (125 * 6) + (i * 125), 800 - 125))
        surface.blit(grass2, (2500 + (125 * 6) + (i * 125), 800 - (125 * 2)))
    # end of slightly high ground
    surface.blit(grass5, (2500 + (125 * 9), 800 - 125))
    surface.blit(grass3, (2500 + (125 * 9), 800 - (125 * 2)))
    surface.blit(grass3, (3750, 800 - 125))
    # parkour!
    surface.blit(grassFloat, (4000, 800 - (125 * 4)))
    surface.blit(grassFloat, (4000 + (125 * 3), 800 - (125 * 3)))
    surface.blit(grassFloat, (4000 + (125 * 5), 800 - (125 * 5)))
    surface.blit(grassFloat, (4000 + (125 * 8), 800 - (125 * 5)))
    surface.blit(grassFloat, (4000 + (125 * 11), 800 - (125 * 4)))
    # end level platform
    for i in range (0,3):
        surface.blit(grass5, (5500 + (i * 125), 800 - 125))
        surface.blit(grass2, (5500 + (i * 125), 800 - (125 * 2)))
    return surface

def drawLevel2(surface):
    surface.fill((0, 0, 0, 0))
    for i in range(0, 10):
        surface.blit(grass2, (i * 125, 800))
    # stepping off
    surface.blit(grassFloat, (1250, 800-125))
    # two long floating
    surface.blit(grassFloat, (1600, 800 - (125 * 2)))
    surface.blit(grassFloat, (1600 + 125, 800 - (125 * 2)))
    # two long floating lower
    surface.blit(grassFloat, (2100, 800 - 125))
    surface.blit(grassFloat, (2100 + 125, 800 - 125))
    # vertical wall
    surface.blit(grass2, (2600, 800 - (125 * 3)))
    surface.blit(grass8, (2600, 800 - (125 * 2)))
    # small floats
    surface.blit(grassFloat, (2900, 800 - (125 * 2)))
    surface.blit(grassFloat, (3200, 800 - (125 * 3)))
    surface.blit(grassFloat, (3700, 800 - 125))
    # last part
    for i in range(0,5):
        surface.blit(grassFloat, (4050 + (i * 125), 800 - (125 * 2)))
    
    return surface

#loading the trash
bottle = transform.scale(image.load("images/trash/Plastic Bottle.png"), (125, 125))
level1Trash = [Trash(bottle), Trash(bottle), Trash(bottle), Trash(bottle), Trash(bottle)]

def drawTrash1(surface):
    surface.fill((0, 0, 0, 0))
    if level1Trash[0].collected == False:
        surface.blit(level1Trash[0].img, (500 + 125, 800 - (2 * 125)))
    if level1Trash[1].collected == False:
        surface.blit(level1Trash[1].img, (0, 0))
    if level1Trash[2].collected == False:
        surface.blit(level1Trash[2].img, (0, 0))
    if level1Trash[3].collected == False:
        surface.blit(level1Trash[3].img, (0, 0))
    if level1Trash[4].collected == False:
        surface.blit(level1Trash[4].img, (0, 0))
    return surface
