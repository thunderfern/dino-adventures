from pygame import *
from objects import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

#initializing the surfaces

xchange, ychange, x, y = 0

waters = []
trashes = []


#just click to exit
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN:
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
    display.flip()
    clock.tick(60)

quit()
