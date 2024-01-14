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

xchange, ychange, x, y = 0, 0, 0, 0

player = Player()
trash1 = Trash()
playerright = PlayerCollisions()
groundSurface = drawLevel2(groundSurface)
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
        x += 5
    if curkeys[K_RIGHT]:
        if playerright.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
            pass
        else:
            x -= 5
   # x = max(0, x)
    #y = max(0, y)
    tmp1, tmp2 = 0, 0
    #if it does collide
    if player.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
        #tmp1, tmp2 = player.mask.overlap(ground.mask, (x, y))
        #print(tmp1, tmp2)
        #print(ground.mask.get_size())
        #print(player.mask.get_size())
        
        if curkeys[K_UP]:
            ychange -= 5
        else:
            ychange = 0
        #print(tmp1, tmp2)
    else:
        ychange += 1
    #if curState == 1:
    #    pass
    y -= ychange
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
    groundSurface = drawLevel2(groundSurface)
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
    draw.rect(screen, "#FF0000", Rect(tmp1, tmp2, 10, 10))
    display.flip()
    clock.tick(60)

quit()
