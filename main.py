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
batter = transform.scale(image.load("images/trash/Battery.png"), (125, 125))

level1Trash = [Trash(bottle), Trash(bag), Trash(bottle), Trash(plastic), Trash(batter), Trash(bag)]

#initializing the surfaces
playerSurface = Surface((width, height)).convert_alpha()
trashCollectionSurface = Surface((width, height))
groundSurface = Surface((10000, 10000)).convert_alpha()
obstacleSurface = Surface((10000, 10000)).convert_alpha()
levelTrashSurface = Surface((10000, 10000)).convert_alpha()
obstacleSurface = Surface((10000, 10000)).convert_alpha()
levelTrashSurface = drawTrash1(levelTrashSurface, level1Trash)

xchange, ychange, x, y = 0, 0, 500, 0

player = Player()
trash1 = Trash(transform.scale(image.load("images/trash/Plastic Bottle.png"), (125, 125)))
playerRight = PlayerCollisions("images/player/Collide Right.png")
playerLeft = PlayerCollisions("images/player/Collide Left.png")
playerTop = PlayerCollisions("images/player/Collide Top.png")
playerBot = PlayerCollisions("images/player/Collide Bot.png")
groundSurface = drawLevel1(groundSurface)
obstacleSurface = drawObstacle1(obstacleSurface)
ground = Ground(groundSurface)
obstacle = Obstacle(obstacleSurface)

waters = []
trashes = []
trashCollection = [trash1, trash1, trash1, trash1]

#1 is start screen, 2 is trash collection screen
curState = 2

#curState 1

#curState 2
trashState = 0

#just click to exit
run = True
doublejump = False
justjumped = False
while run:
    justjumped = False
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
    
    if curkeys[K_LEFT] or curkeys[K_a]:
        if playerLeft.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
            x += 10
        player.setOrientation(1)
    if curkeys[K_RIGHT] or curkeys[K_d]:
        if playerRight.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
            x -= 10
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
    else:
        ychange += 2
    y -= ychange

    if playerTop.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
        ychange = 2
    
    if player.mask.overlap(obstacle.mask, (x - width / 2, y - height / 2)):
        print("ur sooo dead")
    #if curState == 1:
    #    pass
    if curState == 2:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                mousex, mousey = mouse.get_pos()

        tmp = []
        for i in range(0, 3):
            tmp.append(trashCollection[trashState * 4 + i])
    #trashCollectionSurface = drawTrashCollection(trashCollectionSurface, tmp)
    #screen.blit(trashCollectionSurface, (x, y))
    screen.fill("#000000")
    #groundSurface = drawLevel1(groundSurface)
    screen.blit(groundSurface, (x, y))
    playerSurface = player.drawChar(playerSurface)
    screen.blit(playerSurface, (width / 2, height / 2))
    #screen.blit(playerright.mask.to_surface(), (width / 2, height / 2))
    #print(x, y)
    #levelTrashSurface = drawTrash1(levelTrashSurface)
    screen.blit(levelTrashSurface, (x, y))
    screen.blit(obstacleSurface, (x, y))
    player.updateState()
    display.flip()
    clock.tick(60)

quit()
