from pygame import *
from objects import *
from drawFunctions import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

#initializing the surfaces
trashCollectionSurface = Surface((width, height))
groundSurface = Surface((width, height))
playerSurface = Surface((width, height)).convert_alpha()

xchange, ychange, x, y = 0, 0, 0, 0

player = Player()
trash1 = Trash()

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
            if e.key == K_RIGHT:
                x -= 10
            if e.key == K_LEFT:
                x += 10
            if e.key == K_SPACE:
                y += 10
    #if curState == 1:
    #    pass
    if curState == 2:
        screen.blit(trashCollectionSurface, (0, 0))
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                mousex, mousey = mouse.get_pos()

        tmp = []
        for i in range(0, 3):
            tmp.append(trashCollection[trashState * 4 + i])
        trashCollectionSurface = drawTrashCollection(trashCollectionSurface, tmp)
        screen.blit(trashCollectionSurface, (0, 0))
        playerSurface = player.drawChar(playerSurface)
        screen.blit(playerSurface, (0, 0))
    #    pass
    display.flip()
    clock.tick(60)

quit()
