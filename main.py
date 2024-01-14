from pygame import *
from objects import *
from drawFunctions import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()
font.init()
my_font = font.SysFont('Comic Sans MS', 18)

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
treasureSurface = Surface((10000, 10000)).convert_alpha()
treasureSurface.fill((0, 0, 0, 0))

xchange, ychange, x, y = 0, 0, 500, 0

player = Player()
playerRight = PlayerCollisions("images/player/Collide Right.png")
playerLeft = PlayerCollisions("images/player/Collide Left.png")
playerTop = PlayerCollisions("images/player/Collide Top.png")
playerBot = PlayerCollisions("images/player/Collide Bot.png")

trashes = []
trashCollection = [Trash(bottle, (0, 0)), Trash(bag, (0, 0)), Trash(plastic, (0, 0)), Trash(battery, (0, 0))]

#1 is start screen, 2 is trash collection screen
curState = 1
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
levelreset = level
playbutton = Button("images/buttons/Play Button Normal State.png", "images/buttons/Play Button Hover State.png", 125)
inventorybutton = Button("images/buttons/Inventory Normal.png", "images/buttons/Inventory Hover.png", 125)
mouseblock = Mouse()
treasure = Treasure()
backgroundsurf = Surface((10000, 10000)).convert_alpha()
backgroundsurf.blit(transform.scale(image.load("images/Placeholder BG.png"), (19200 / 2, 10800 / 2)), (0, 0))
#1920, 1080
mousebuttondown = False
mousebuttonup = True
upkey = False
rightkey = False
downkey = False
leftkey = False
spacekey = False
while run:
    mousebuttondown = False
    upkey = False
    rightkey = False
    downkey = False
    leftkey = False
    spacekey = False
    for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False
                if e.key == K_UP or e.key == K_w:
                    upkey = True
                if e.key == K_SPACE:
                    spacekey = True
            if e.type == MOUSEBUTTONDOWN and mousebuttonup == True:
                mousebuttondown = True
                mousebuttonup = False
            if e.type == MOUSEBUTTONUP:
                mousebuttonup = True
            #200/128
    if curState == 1:
        mousex, mousey = mouse.get_pos()
        screen.blit(transform.scale(image.load("images/home page.png"), (width, width / 200 * 128)).convert_alpha(), (0, 0))
        if playbutton.mask.overlap(mouseblock.mask, (width / 2 + 125 / 2 - mousex, height / 2 + 125 / 2 - mousey)):
            screen.blit(playbutton.hoverimg, (width / 2 - 125 / 2, height / 2 - 125 / 2))
            if mousebuttondown:
                curState = 3
        else:
            screen.blit(playbutton.img, (width / 2 - 125 / 2, height / 2 - 125 / 2))

    elif curState == 2:
        mousex, mousey = mouse.get_pos()
        screen.fill("#FFFFFF")
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
        textBag = my_font.render('Is it a bird? Is it a jellyfish? No! It’s a… plastic bag? The appearance of plastic bags resembles many plants and prey in some animals’ diets.', False, (0, 0, 0))
        textBag = my_font.render('Is it a bird? Is it a jellyfish? No! It’s a… plastic bag? The appearance of plastic bags resembles many plants and prey in some animals’ diets.', False, (0, 0, 0))
        textBag = my_font.render('Is it a bird? Is it a jellyfish? No! It’s a… plastic bag? The appearance of plastic bags resembles many plants and prey in some animals’ diets.', False, (0, 0, 0))
        textBag = my_font.render('Is it a bird? Is it a jellyfish? No! It’s a… plastic bag? The appearance of plastic bags resembles many plants and prey in some animals’ diets.', False, (0, 0, 0))
        textBag = my_font.render('Is it a bird? Is it a jellyfish? No! It’s a… plastic bag? The appearance of plastic bags resembles many plants and prey in some animals’ diets.', False, (0, 0, 0))

        textPlastic = my_font.render('Fishing nets lost at sea often get caught on animals in water, potentially injuring them and preventing mammals and birds from rising to the surface to breathe.', False, (0, 0, 0))
        textBatter = my_font.render('E-waste is the fastest growing type of solid waste. Trash such as batteries leak toxic chemicals into its environment which are extremely harmful to plants and animals.', False, (0, 0, 0))
        if trashCollection[0].collected:
            img1 = Surface((1000, 1000)).convert_alpha()
            img1.fill((0, 0, 0, 0))
            img1.blit(unlocked, (0, 0))
            img1.blit(bottle, (0, 0))
            img1.blit(textBottle, (70, 70))
            img1.blit(textBottle1, (70, 120))
            img1.blit(textBottle2, (70, 170))
            img1.blit(textBottle3, (70, 220))
            img1.blit(textBottle4, (70, 270))
        if trashCollection[1].collected:
            img2 = Surface((1000, 1000)).convert_alpha()
            img2.fill((0, 0, 0, 0))
            img2.blit(unlocked, (0, 0))
            img2.blit(bag, (0, 0))
            img2.blit(textBag, (0,0))
        if trashCollection[2].collected:
            img3 = Surface((1000, 1000)).convert_alpha()
            img3.fill((0, 0, 0, 0))
            img3.blit(unlocked, (0, 0))
            img3.blit(plastic, (0, 0))
            img3.blit(textPlastic, (0,0))
        if trashCollection[3].collected:
            img4 = Surface((1000, 1000)).convert_alpha()
            img4.fill((0, 0, 0, 0))
            img4.blit(unlocked, (0, 0))
            img4.blit(battery, (0, 0))
            img4.blit(textBatter, (0,0))
        screen.blit(img1, (width / 7, height / 12))
        screen.blit(img2, (width / 7 * 2 + height / 5 * 2, height / 12))
        screen.blit(img3, (width / 7, height / 12 * 2 + height / 5 * 2))
        screen.blit(img4, (width / 7 * 2 + height / 5 * 2, height / 12 * 2 + height / 5 * 2))
        if inventorybutton.mask.overlap(mouseblock.mask, (width - mousex - 25, -25 + mousey)):
            screen.blit(inventorybutton.hoverimg, (width - 150, 25))
            if mousebuttondown:
                curState = 3
        else:
            screen.blit(inventorybutton.img, (width - 150, 25))
        tmp = []
        for i in range(0, 3):
            tmp.append(trashCollection[trashState * 4 + i])
    elif curState == 3:
        justjumped = False
        scaling = False
        if levelreset == 1:
            for t in level1Trash:
                t.collected = False
            groundSurface = drawLevel1(groundSurface)
            obstacleSurface = drawObstacle1(obstacleSurface)
            levelTrashSurface = drawTrash1(levelTrashSurface, level1Trash)
            treasureSurface.fill((0, 0, 0, 0))
            treasureSurface.blit(treasure.img, (7450, 1050))
            x = 500
            y = 0
            ychange = 0
            ground = Ground(groundSurface)
            obstacle = Obstacle(obstacleSurface)
            trash = TrashLayer(levelTrashSurface)
        elif levelreset == 2:
            for t in level2Trash:
                t.collected = False
            groundSurface = drawLevel2(groundSurface)
            obstacleSurface = drawObstacle2(obstacleSurface)
            levelTrashSurface = drawTrash2(levelTrashSurface, level2Trash)
            x = 500
            y = 0
            ychange = 0
            ground = Ground(groundSurface)
            obstacle = Obstacle(obstacleSurface)
            trash = TrashLayer(levelTrashSurface)

        levelreset = 0

        curkeys = key.get_pressed()
        player.setScaling(0)

        #if curkeys[K_SPACE]:
            #y += 10
        
        if spacekey and player.player == 1 and xchange == 0:
            if player.orientation == 1:
                xchange = 25
            else:
                xchange = -25
        if (xchange > 0):
            xchange -= 1
        elif xchange < 0:
            xchange += 1

        if curkeys[K_1]:
            player.change(1)
        if curkeys[K_2]:
            player.change(2)
        if curkeys[K_3]:
            player.change(3)
        if upkey:
            if playerBot.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
                ychange = -25
                justjumped = True
            elif doublejump == False and player.player == 0:
                ychange = -25
                doublejump = True
                justjumped = True
        
        if curkeys[K_LEFT] or curkeys[K_a]:
            if playerLeft.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
                x += 10
                x += xchange
            else:
                if player.player == 2:
                    if curkeys[K_UP] or curkeys[K_w]:
                        player.setScaling(1)
                        scaling = True
                        y += 10
            player.setOrientation(1)
        elif curkeys[K_RIGHT] or curkeys[K_d]:
            if playerRight.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
                x -= 10
                x += xchange
            else:
                if player.player == 2:
                    if curkeys[K_UP] or curkeys[K_w]:
                        player.setScaling(2)
                        scaling = True
                        y += 10
            player.setOrientation(0)
        elif curkeys[K_SPACE]:
            if player.orientation == 1:
                if playerLeft.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
                    x += 10
                    x += xchange
            else:
                if playerRight.mask.overlap(ground.mask, (x - width / 2, y - height / 2)) == None:
                    x -= 10
                    x += xchange
        
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
        if xchange != 0:
            ychange = 0
        y -= ychange

        if playerTop.mask.overlap(ground.mask, (x - width / 2, y - height / 2)):
            ychange = 2
        
        if player.mask.overlap(obstacle.mask, (x - width / 2, y - height / 2)):
            levelreset = level
        
        if player.mask.overlap(treasure.mask, (x - width / 2 + 7450, y - height / 2 + 1050)):
            level += 1
            levelreset = level

        #screen.fill("#000000")

        #trashCollectionSurface = drawTrashCollection(trashCollectionSurface, tmp)
        #screen.blit(trashCollectionSurface, (x, y))
        
        #groundSurface = drawLevel1(groundSurface)
        screen.blit(backgroundsurf, (x - 500, y - 3500))
        screen.blit(groundSurface, (x, y))
        playerSurface = player.drawChar(playerSurface)
        screen.blit(playerSurface, (width / 2, height / 2))
        screen.blit(treasureSurface, (x, y))
        #
        #print(x, y)
        #levelTrashSurface = drawTrash1(levelTrashSurface)
        
        #screen.blit(levelTrashSurface, (x, y))
        screen.blit(obstacleSurface, (x, y))
        if ychange != 0:
            player.state = 0
        elif curkeys[K_LEFT] or curkeys[K_RIGHT] or curkeys[K_UP] or curkeys[K_w] or curkeys[K_a] or curkeys[K_d] or xchange != 0:
            player.updateState()
        else:
            player.state = 8
        if level == 1:
            for i in range(0, len(level1Trash)):
                #screen.blit(level1Trash[i].mask.to_surface(), (x + level1Trash[i].x, y + level1Trash[i].y))
                if level1Trash[i].collected:
                    continue
                if (player.mask.overlap(level1Trash[i].mask, (x + level1Trash[i].x - width / 2, y + level1Trash[i].y - height / 2))):
                    level1Trash[i].collected = True
                    levelTrashSurface = drawTrash1(levelTrashSurface, level1Trash)
                    if level1Trash[i].img == bottle:
                        trashCollection[0].collected = True
                    if level1Trash[i].img == bag:
                        trashCollection[1].collected = True
                    if level1Trash[i].img == plastic:
                        trashCollection[2].collected = True
                    if level1Trash[i].img == battery:
                        trashCollection[3].collected = True
        else:
            for i in range(0, len(level2Trash)):
                #screen.blit(level1Trash[i].mask.to_surface(), (x + level1Trash[i].x, y + level1Trash[i].y))
                if level2Trash[i].collected:
                    continue
                if (player.mask.overlap(level2Trash[i].mask, (x + level2Trash[i].x - width / 2, y + level2Trash[i].y - height / 2))):
                    level2Trash[i].collected = True
                    levelTrashSurface = drawTrash1(levelTrashSurface, level2Trash)
                    if level2Trash[i].img == bottle:
                        trashCollection[0].collected = True
                    if level2Trash[i].img == bag:
                        trashCollection[1].collected = True
                    if level2Trash[i].img == plastic:
                        trashCollection[2].collected = True
                    if level2Trash[i].img == battery:
                        trashCollection[3].collected = True
        screen.blit(levelTrashSurface, (x, y))

        #inventory button
        mousex, mousey = mouse.get_pos()
        if inventorybutton.mask.overlap(mouseblock.mask, (width - mousex - 25, -25 + mousey)):
            screen.blit(inventorybutton.hoverimg, (width - 150, 25))
            if mousebuttondown:
                curState = 2
        else:
            screen.blit(inventorybutton.img, (width - 150, 25))
    display.flip()
    clock.tick(60)

quit()
