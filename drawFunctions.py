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