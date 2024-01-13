from pygame import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

run = True

while run:
    display.flip()
    clock.tick(60)

quit()
