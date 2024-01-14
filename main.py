from pygame import *
from objects import *
from drawFunctions import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

#initializing the surfaces
trashCollectionSurface = Surface((width, height))
groundSurface = Surface((10000, 10000)).convert_alpha()
playerSurface = Surface((width, height)).convert_alpha()

xchange, ychange, x, y = 0, 0, 500, 0

player = Player()
trash1 = Trash()
playerRight = PlayerCollisions("images/player/Collide Right.png")
playerLeft = PlayerCollisions("images/player/Collide Left.png")
playerTop = PlayerCollisions("images/player/Collide Top.png")
playerBot = PlayerCollisions("images/player/Collide Bot.png")
groundSurface = drawLevel1(groundSurface)
ground = Ground(groundSurface)

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
while run:
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
    curkeys = key.get_pressed()
    
    if curkeys[K_LEFT]:
        if playerLeft.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
            x += 10
        player.setOrientation(1)
    if curkeys[K_RIGHT]:
        if playerRight.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
            x -= 10
        player.setOrientation(0)
    if curkeys[K_UP]:
        if playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
            ychange -= 25
    y -= ychange
    if playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
        ychange = 0
    else:
        ychange += 2
    if playerTop.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
        ychange = 2
    
   # x = max(0, x)
    #y = max(0, y)
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
    groundSurface = drawLevel1(groundSurface)
    screen.blit(groundSurface, (x, y))
    playerSurface = player.drawChar(playerSurface)
    screen.blit(playerSurface, (width / 2, height / 2))
    #screen.blit(playerright.mask.to_surface(), (width / 2, height / 2))
    #print(x, y)
    player.updateState()
    #player.updateMask(x, y)
    #screen.blit(ground.mask.to_surface(), (0, 0))
    #screen.blit(player.mask.to_surface(), (x, y))
    #    pass
    display.flip()
    clock.tick(60)

quit()
