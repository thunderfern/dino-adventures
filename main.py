from pygame import *
from objects import *
from drawFunctions import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

#trash
bottle = transform.scale(image.load("images/trash/Plastic Bottle.png"), (125, 125))
bag = transform.scale(image.load("images/trash/Plastic Bag.png"), (125, 125))
plastic = transform.scale(image.load("images/trash/Microplastic.png"), (125, 125))
battery = transform.scale(image.load("images/trash/Battery.png"), (125, 125))

level1Trash = [Trash(bottle, (500 + 125, 800 - (125 * 3.5))), 
               Trash(bag, (1800, 800 - (125 * 3))), 
               Trash(bottle, (2700, 800 - (125 * 5))), 
               Trash(plastic, (2500 + (125 * 6.5), 800 - (125 * 4))), 
               Trash(battery, (4000 + (125 * 2), 800 - (125 * 6))), 
               Trash(bag, (4000 + (125 * 10), 800 - (125 * 5)))]
level2Trash = [Trash(bag, (125 * 6, 800 - (125 * 2))), 
               Trash(battery, (1800, 800 - (125 * 4))), 
               Trash(bottle, (2475, 800 - (125 * 3))), 
               Trash(plastic, (3100, 800 - (125 * 5))), 
               Trash(battery, (3700, 800 - (125 * 3))), 
               Trash(bag, (4300, 800 - (125 * 4)))]

#initializing the surfaces
playerSurface = Surface((width, height)).convert_alpha()
trashCollectionSurface = Surface((width, height))
groundSurface = Surface((10000, 10000)).convert_alpha()
obstacleSurface = Surface((10000, 10000)).convert_alpha()
levelTrashSurface = Surface((10000, 10000)).convert_alpha()
obstacleSurface = Surface((10000, 10000)).convert_alpha()

xchange, ychange, x, y = 0, 0, 500, 0

player = Player()
trash1 = Trash(transform.scale(image.load("images/trash/Plastic Bottle.png"), (125, 125)), (0, 0))
playerRight = PlayerCollisions("images/player/Collide Right.png")
playerLeft = PlayerCollisions("images/player/Collide Left.png")
playerTop = PlayerCollisions("images/player/Collide Top.png")
playerBot = PlayerCollisions("images/player/Collide Bot.png")

waters = []
trashes = []
trashCollection = [trash1, trash1, trash1, trash1]

#1 is start screen, 2 is trash collection screen
curState = 2
level = 1

#curState 1

#curState 2
trashState = 0

#just click to exit
run = True
doublejump = False
justjumped = False
scaling = False
if level == 1:
    groundSurface = drawLevel1(groundSurface)
    obstacleSurface = drawObstacle1(obstacleSurface)
    levelTrashSurface = drawTrash1(levelTrashSurface, level1Trash)
else:
    groundSurface = drawLevel2(groundSurface)
    obstacleSurface = drawObstacle2(obstacleSurface)
    levelTrashSurface = drawTrash2(levelTrashSurface, level2Trash)
ground = Ground(groundSurface)
obstacle = Obstacle(obstacleSurface)
trash = TrashLayer(levelTrashSurface)
levelreset = 1
while run:
    justjumped = False
    scaling = False
    if levelreset == 1:
        for t in level1Trash:
            t.collected = False
        groundSurface = drawLevel1(groundSurface)
        obstacleSurface = drawObstacle1(obstacleSurface)
        levelTrashSurface = drawTrash1(levelTrashSurface, level1Trash)
        x = 500
        y = 0
        ychange = 0
    elif levelreset == 2:
        for t in level2Trash:
            t.collected = False
        groundSurface = drawLevel2(groundSurface)
        obstacleSurface = drawObstacle2(obstacleSurface)
        levelTrashSurface = drawTrash2(levelTrashSurface, level2Trash)
        x = 500
        y = 0
        ychange = 0

    levelreset = 0
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_SPACE:
                y += 10
            if e.key == K_1:
                player.change(1)
            if e.key == K_2:
                player.change(2)
            if e.key == K_3:
                player.change(3)
            if e.key == K_UP or e.key == K_w:
                if playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
                    ychange = -25
                    justjumped = True
                elif doublejump == False and player.player == 0:
                    ychange = -25
                    doublejump = True
                    justjumped = True

    curkeys = key.get_pressed()
    player.setScaling(0)
    
    if curkeys[K_LEFT] or curkeys[K_a]:
        if playerLeft.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
            x += 10
        else:
            if player.player == 2:
                if curkeys[K_UP] or curkeys[K_w]:
                    player.setScaling(1)
                    scaling = True
                    y += 10
        player.setOrientation(1)
    if curkeys[K_RIGHT] or curkeys[K_d]:
        if playerRight.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
            x -= 10
        else:
            if player.player == 2:
                if curkeys[K_UP] or curkeys[K_w]:
                    player.setScaling(2)
                    scaling = True
                    y += 10
        player.setOrientation(0)
    #if curkeys[K_UP]:
        #if playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
            #ychange -= 25
    if playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) and justjumped == False:
        while playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
            y += 1
        ychange = 0
        doublejump = False
        y -= 1
    elif scaling:
        ychange = 0
    else:
        ychange += 2
    y -= ychange

    if playerTop.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
        ychange = 2
    
    if player.mask.overlap(obstacle.mask, (x - width / 2, y - height / 2)):
        levelreset = level
    
    #if curState == 1:
    #    pass
    if curState == 2:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                mousex, mousey = mouse.get_pos()

        tmp = []
        for i in range(0, 3):
            tmp.append(trashCollection[trashState * 4 + i])
    
    screen.fill("#000000")

    #trashCollectionSurface = drawTrashCollection(trashCollectionSurface, tmp)
    #screen.blit(trashCollectionSurface, (x, y))
    
    #groundSurface = drawLevel1(groundSurface)
    
    screen.blit(groundSurface, (x, y))
    playerSurface = player.drawChar(playerSurface)
    screen.blit(playerSurface, (width / 2, height / 2))
    #
    #print(x, y)
    #levelTrashSurface = drawTrash1(levelTrashSurface)
    
    #screen.blit(levelTrashSurface, (x, y))
    screen.blit(obstacleSurface, (x, y))
    player.updateState()
    if level == 1:
        for i in range(0, len(level1Trash)):
            #screen.blit(level1Trash[i].mask.to_surface(), (x + level1Trash[i].x, y + level1Trash[i].y))
            if level1Trash[i].collected:
                continue
            if (player.mask.overlap(level1Trash[i].mask, (x + level1Trash[i].x - width / 2, y + level1Trash[i].y - height / 2))):
                level1Trash[i].collected = True
                levelTrashSurface = drawTrash1(levelTrashSurface, level1Trash)
    else:
        for i in range(0, len(level2Trash)):
            #screen.blit(level1Trash[i].mask.to_surface(), (x + level1Trash[i].x, y + level1Trash[i].y))
            if level2Trash[i].collected:
                continue
            if (player.mask.overlap(level2Trash[i].mask, (x + level2Trash[i].x - width / 2, y + level2Trash[i].y - height / 2))):
                level2Trash[i].collected = True
                levelTrashSurface = drawTrash1(levelTrashSurface, level2Trash)

    screen.blit(levelTrashSurface, (x, y))
    display.flip()
    clock.tick(60)

quit()
