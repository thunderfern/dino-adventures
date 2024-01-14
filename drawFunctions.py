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
grassFloatR = transform.scale(image.load("images/blocks/grass block float right.png"), (125, 125))
grassFloatM = transform.scale(image.load("images/blocks/grass block float middle.png"), (125, 125))
grassFloatL = transform.scale(image.load("images/blocks/grass block float left.png"), (125, 125))
grassTop = transform.scale(image.load("images/blocks/grass block top.png"), (125, 125))
grassMiddle = transform.scale(image.load("images/blocks/grass block middle.png"), (125, 125))
fleshFloat = transform.scale(image.load("images/blocks/flesh block float.png"), (125, 125))
fleshFloatR = transform.scale(image.load("images/blocks/flesh block float right.png"), (125, 125))
fleshFloatM = transform.scale(image.load("images/blocks/flesh block float middle.png"), (125, 125))
fleshFloatL = transform.scale(image.load("images/blocks/flesh block float left.png"), (125, 125))
whale = transform.scale(image.load("images/Whale Body.png"), (3000, 1500))


def drawLevel1(surface):
    surface.fill((0, 0, 0, 0))
    # draw wall barrier
    for i in range (0, 6):
        surface.blit(grassMiddle, (0, 800 - (125 * i)))
    surface.blit(grassTop, (0, 800 - (125 * 6)))
    # draw ground
    for i in range(0, 50):
        surface.blit(grass2, (i * 125, 800))
    # floating bit
        surface.blit(grassFloatL, (500, 500))
        surface.blit(grassFloatM, (500 + 125, 500))
        surface.blit(grassFloatR, (500 + (125 * 2), 500))
    # small vertical
    surface.blit(grassTop, (1300, 800 - 125))
    # medium vertical
    surface.blit(grass4, (1800, 800 - 125))
    surface.blit(grassTop, (1800, 800 - (125 * 2)))
    # small vert
    surface.blit(grass3, (1800 + 125, 800 - 125))
    # large vertical ground
    surface.blit(grass4, (2500, 800 - 125))
    surface.blit(grass4, (2500, 800 - (125 * 2)))
    surface.blit(grass1, (2500, 800 - (125 * 3)))
    # high ground
    for i in range (0,4):
        surface.blit(grass5, (2500 + 125 + (i * 125), 800 - 125))
        surface.blit(grass5, (2500 + 125 + (i * 125), 800 - (125 * 2)))
        surface.blit(grass2, (2500 + 125 + (i * 125), 800 - (125 * 3)))
    surface.blit(grass5, (2500 + 125 + (4 * 125), 800 - 125))
    surface.blit(grass5, (2500 + 125 + (4 * 125), 800 - (125 * 2)))
    surface.blit(grass3, (2500 + 125 + (4 * 125), 800 - (125 * 3)))
    # high floating blocks (headbump)
    surface.blit(grassFloatL, (2500 + (125 * 5), 800 - (125 * 5)))
    surface.blit(grassFloatM, (2500 + (125 * 6), 800 - (125 * 5)))
    surface.blit(grassFloatM, (2500 + (125 * 7), 800 - (125 * 5)))
    surface.blit(grassFloatR, (2500 + (125 * 8), 800 - (125 * 5)))
    # slightly high ground
    surface.blit(grass5, (2500 + (125 * 6), 800 - 125))
    surface.blit(grass2, (2500 + (125 * 6), 800 - (125 * 2)))
    surface.blit(grass5, (2500 + (125 * 7), 800 - 125))
    surface.blit(grass2, (2500 + (125 * 7), 800 - (125 * 2)))
    # high ground
    surface.blit(grass5, (2500 + (125 * 8), 800 - 125))
    surface.blit(grass5, (2500 + (125 * 8), 800 - (125 * 2)))
    surface.blit(grass1, (2500 + (125 * 8), 800 - (125 * 3)))
    # end of high ground
    surface.blit(grass5, (2500 + (125 * 9), 800 - 125))
    surface.blit(grass6, (2500 + (125 * 9), 800 - (125 * 2)))
    surface.blit(grass3, (2500 + (125 * 9), 800 - (125 * 3)))
    # step
    surface.blit(grass3, (3750, 800 - 125))
    # headbump
    surface.blit(grassFloat, (4000, 800 - (125 * 6)))
    surface.blit(grassFloat, (4000 + 125, 800 - (125 * 6)))
    # parkour!
    surface.blit(grassFloat, (4000, 800 - (125 * 4)))
    surface.blit(grassFloat, (4000 + (125 * 3), 800 - (125 * 3)))
    surface.blit(grassFloat, (4000 + (125 * 5), 800 - (125 * 5)))
    surface.blit(grassFloat, (4000 + (125 * 8), 800 - (125 * 3)))
    #vertical bit
    surface.blit(grassTop, (4000 + (125 * 11), 800 - (125 * 6)))
    surface.blit(grassMiddle, (4000 + (125 * 11), 800 - (125 * 5)))
    surface.blit(grassMiddle, (4000 + (125 * 11), 800 - (125 * 4)))
    surface.blit(grassMiddle, (4000 + (125 * 11), 800 - (125 * 3)))
    surface.blit(grass4, (4000 + (125 * 11), 800 - (125 * 2)))
    surface.blit(grass4, (4000 + (125 * 11), 800 - 125))
    # end level platform
    for i in range (0,3):
        surface.blit(grass5, (5500 + (i * 125), 800 - 125))
        surface.blit(grass2, (5500 + (i * 125), 800 - (125 * 2)))
    surface.blit(whale, (5500 + 125, 800 - (125 * 10) + 400))
    return surface

def drawLevel2(surface):
    surface.fill((0, 0, 0, 0))
    for i in range(0, 10):
        surface.blit(fleshFloatM, (i * 125, 800))
    # stepping off piece
    surface.blit(fleshFloat, (1250, 800-125))
    # two-long floating
    surface.blit(fleshFloatL, (1600, 800 - (125 * 2)))
    surface.blit(fleshFloatR, (1600 + 125, 800 - (125 * 2)))
    # two-long floating lower
    surface.blit(fleshFloatL, (2100, 800 - 125))
    surface.blit(fleshFloatR, (2100 + 125, 800 - 125))
    # vertical wall
    surface.blit(fleshFloat, (2600, 800 - (125 * 2.75)))
    surface.blit(fleshFloat, (2600, 800 - (125 * 2)))
    # small floats
    surface.blit(fleshFloat, (2900, 800 - (125 * 2)))
    surface.blit(fleshFloat, (3200, 800 - (125 * 3)))
    surface.blit(fleshFloat, (3700, 800 - 125))
    # last part
    surface.blit(fleshFloatL, (4050, 800 - (125 * 2)))
    for i in range(1,7):
        surface.blit(fleshFloatM, (4050 + (i * 125), 800 - (125 * 2)))
    surface.blit(fleshFloatR, (4050 + (7 * 125), 800 - (125 * 2)))
    
    return surface

#loading the trash
bottle = transform.scale(image.load("images/trash/Plastic Bottle.png"), (125, 125))
bag = transform.scale(image.load("images/trash/Plastic Bag.png"), (125, 125))
plastic = transform.scale(image.load("images/trash/Microplastic.png"), (125, 125))
battery = transform.scale(image.load("images/trash/Battery.png"), (125, 125))

def drawTrash1(surface, level1Trash):
    surface.fill((0, 0, 0, 0))
    for t in level1Trash:
        if t.collected == False:
            surface.blit(t.img, (t.x, t.y))
    '''if level1Trash[0].collected == False:
        surface.blit(level1Trash[0].img, (500 + 125, 800 - (125 * 3.5)))
    if level1Trash[1].collected == False:
        surface.blit(level1Trash[1].img, (1800, 800 - (125 * 3)))
    if level1Trash[2].collected == False:
        surface.blit(level1Trash[2].img, (2700, 800 - (125 * 5)))
    if level1Trash[3].collected == False:
        surface.blit(level1Trash[3].img, (2500 + (125 * 7.5), 800 - (125 * 6)))
    if level1Trash[4].collected == False:
        surface.blit(level1Trash[4].img, (4000 + (125 * 2), 800 - (125 * 6)))
    if level1Trash[5].collected == False:
        surface.blit(level1Trash[5].img, (4000 + (125 * 10), 800 - (125 * 5)))'''
    return surface


def drawTrash2(surface, level2Trash):
    surface.fill((0, 0, 0, 0))
    if level2Trash[0].collected == False:
        surface.blit(level2Trash[0].img, (125 * 6, 800 - (125 * 2)))
    if level2Trash[1].collected == False:
        surface.blit(level2Trash[1].img, (1800, 800 - (125 * 4)))
    if level2Trash[2].collected == False:
        surface.blit(level2Trash[2].img, (2475, 800 - (125 * 3)))
    if level2Trash[3].collected == False:
        surface.blit(level2Trash[3].img, (3100, 800 - (125 * 4)))
    if level2Trash[4].collected == False:
        surface.blit(level2Trash[4].img, (3700, 800 - (125 * 3)))
    if level2Trash[5].collected == False:
        surface.blit(level2Trash[5].img, (4300, 800 - (125 * 4)))
    return surface

#loading the spikes
        
spike = transform.scale(image.load("images/Spikes.png"), (125, 125))
def drawObstacle1(surface):
    surface.fill((0, 0, 0, 0))
    surface.blit(spike, (0, 800 - (125 * 7)))
    surface.blit(spike, (1800 - 125, 800 - 125))
    surface.blit(spike, (2700, 800 - (125 * 4)))
    surface.blit(spike, (2500 + (125 * 5), 800 - (125 * 6)))
    surface.blit(spike, (2500 + (125 * 6), 800 - (125 * 6)))
    surface.blit(spike, (2500 + (125 * 7), 800 - (125 * 6)))
    surface.blit(spike, (2500 + (125 * 8), 800 - (125 * 6)))
    surface.blit(spike, ((2500 + (125 * 6), 800 - (125 * 3))))
    surface.blit(spike, ((2500 + (125 * 7), 800 - (125 * 3))))
    surface.blit(spike, (4000, 800 - (125 * 7)))
    surface.blit(spike, (4000 + 125, 800 - (125 * 7)))
    for i in range(0, 6):
        surface.blit(spike, (4000 + (125 * i * 2), 800 - 125))
    return surface

def drawObstacle2(surface):
    surface.fill((0, 0, 0, 0))
    surface.blit(spike, (125 * 6, 800 - 125))
    surface.blit(spike, (1600 + 125, 800 - (125 * 3)))
    surface.blit(spike, (2100 + 125, 800 - (125 * 2)))
    surface.blit(spike, (4300, 800 - (125 * 3)))
    for i in range(0,40):
        surface.blit(spike, (i * 125, 1125))
    return surface

def drawText(screen, trashCollection, my_font, width, height):
    
    locked = transform.scale(image.load("images/Locked.png"), (height / 5 * 2, height / 5 * 2)).convert_alpha()
    unlocked = transform.scale(image.load("images/Unlocked.png"), (height / 5 * 2, height / 5 * 2)).convert_alpha()
    img1 = locked
    img2 = locked
    img3 = locked
    img4 = locked
    #img1, img2, img3, img4 = locked, locked, locked, locked
    # inventory descriptions
    textBottle = my_font.render('It can take over 400 years for', False, (0, 0, 0))
    textBottle1 = my_font.render('plastic bottles to biodegrade.', False, (0, 0, 0))
    textBottle2 = my_font.render('In the past 60 years, 6.3', False, (0, 0, 0))
    textBottle3 = my_font.render('billion tons of plastic', False, (0, 0, 0))
    textBottle4 = my_font.render('became plastic waste.', False, (0, 0, 0))
    textBag = my_font.render('Is it a bird? Is it a ', False, (0, 0, 0))
    textBag1 = my_font.render('jellyfish? No! It’s a… ', False, (0, 0, 0))
    textBag2 = my_font.render('plastic bag? The appearance', False, (0, 0, 0))
    textBag3 = my_font.render('of plastic bags resembles', False, (0, 0, 0))
    textBag4 = my_font.render('many plants and prey in', False, (0, 0, 0))
    textBag5 = my_font.render('some animals’ diets.', False, (0, 0, 0))
    textPlastic = my_font.render('As plastic decomposes, it', False, (0, 0, 0))
    textPlastic1 = my_font.render('breaks down into very small', False, (0, 0, 0))
    textPlastic2 = my_font.render('pieces called microplastics.', False, (0, 0, 0))
    textPlastic3 = my_font.render('Due to their inability to be', False, (0, 0, 0))
    textPlastic4 = my_font.render('filtered like larger plastics,', False, (0, 0, 0))
    textPlastic5 = my_font.render('they end up in water and', False, (0, 0, 0))
    textPlastic6 = my_font.render('accumulate in organisms.', False, (0, 0, 0))
    textBatter = my_font.render('E-waste is the fastest', False, (0, 0, 0))
    textBatter1 = my_font.render('growing type of solid waste.', False, (0, 0, 0))
    textBatter2 = my_font.render('Trash such as batteries', False, (0, 0, 0))
    textBatter3 = my_font.render('leak toxic chemicals into', False, (0, 0, 0))
    textBatter4 = my_font.render('its environment which are', False, (0, 0, 0))
    textBatter5 = my_font.render('very bad to plants and animals.', False, (0, 0, 0))
    
    if trashCollection[0].collected:
        img1 = Surface((1000, 1000)).convert_alpha()
        img1.fill((0, 0, 0, 0))
        img1.blit(unlocked, (0, 0))
        img1.blit(bottle, (0, 0))
        img1.blit(textBottle, (70 + 20, 70))
        img1.blit(textBottle1, (70 + 20, 120))
        img1.blit(textBottle2, (70 + 20, 170))
        img1.blit(textBottle3, (70 + 20, 220))
        img1.blit(textBottle4, (70 + 20, 270))
    if trashCollection[1].collected:
        img2 = Surface((1000, 1000)).convert_alpha()
        img2.fill((0, 0, 0, 0))
        img2.blit(unlocked, (0, 0))
        img2.blit(bag, (0, 0))
        img2.blit(textBag, (90 + 20, 70))
        img2.blit(textBag1, (90 + 20, 120))
        img2.blit(textBag2, (90 + 20, 170))
        img2.blit(textBag3, (90 + 20, 220))
        img2.blit(textBag4, (90 + 20, 270))
        img2.blit(textBag5, (90 + 20, 320))
    if trashCollection[2].collected:
        img3 = Surface((1000, 1000)).convert_alpha()
        img3.fill((0, 0, 0, 0))
        img3.blit(unlocked, (0, 0))
        img3.blit(plastic, (0, 0))
        img3.blit(textPlastic, (70 + 20, 70))
        img3.blit(textPlastic1, (70 + 20, 120 - 10))
        img3.blit(textPlastic2, (70 + 20, 170 - 20))
        img3.blit(textPlastic3, (70 + 20, 220 - 30))
        img3.blit(textPlastic4, (70 + 20, 270 - 40))
        img3.blit(textPlastic5, (70 + 20, 320 - 50))
        img3.blit(textPlastic6, (70 + 20, 370 - 60))
    if trashCollection[3].collected:
        img4 = Surface((1000, 1000)).convert_alpha()
        img4.fill((0, 0, 0, 0))
        img4.blit(unlocked, (0, 0))
        img4.blit(battery, (0, 0))
        img4.blit(textBatter, (80 + 20, 70))
        img4.blit(textBatter1, (80 + 20, 120 - 10))
        img4.blit(textBatter2, (80 + 20, 170 - 20))
        img4.blit(textBatter3, (80 + 20, 220 - 30))
        img4.blit(textBatter4, (80 + 20, 270 - 40))
        img4.blit(textBatter5, (80 + 20, 320 - 50))
    screen.blit(img1, (width / 7, height / 12))
    screen.blit(img2, (width / 7 * 2 + height / 5 * 2, height / 12))
    screen.blit(img3, (width / 7, height / 12 * 2 + height / 5 * 2))
    screen.blit(img4, (width / 7 * 2 + height / 5 * 2, height / 12 * 2 + height / 5 * 2))
