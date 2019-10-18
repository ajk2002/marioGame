import math, random, sys
import pygame
from pygame.locals import *


# exit the program
def events():
	for event in pygame.event.get():        
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
			
def jump(jumpCount, playerPosY):
        playerPosY -= (jumpCount ** 2) * 0.5
        jumpCount -= 1
        return jumpCount, playerPosY

def fall(fallCount, playerPosY):
        playerPosY += (fallCount ** 2) * 0.5
        if fallCount < 10:
                fallCount += 1
        return fallCount, playerPosY

# this should check if we are stood on the ground or on a block
# would be better if all blocks were objects within a list, so you could loop through them etc.
def shouldBeFalling(playerPosX, playerPosY):
        if playerPosY >= 500:
                # we're on the ground so not falling
                return (500, False)
        elif playerPosX > 175 and playerPosX < 238 and playerPosY >= 348:
                # we're on the first block so not falling
                return (348, False)
        elif playerPosX > 275 and playerPosX < 338 and playerPosY >= 248 and playerPosY <= 300:
                # we're on the second block so not falling
                return (248, False)
        else:
                return (playerPosY, True)
        brick = Brick().brickdraw()






def redrawGameWindow(playerPosX):
        
        
        bg = pygame.image.load("resized_mountains.png").convert()
        bg1 = pygame.image.load("newmountain.png").convert()
       
        DS.blit(bg, (0,0))
        if playerPosX >= 500:
                playerPosX -= 500
                DS.blit(bg1, (0,0))
                
        DS.blit(char, (playerPosX, playerPosY))
        DS.blit(brick, (200, 400))
        DS.blit(brick2, (300, 300))
        
                



        
# define display surface			
W, H = 600, 600
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
global DS
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 30

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

# load some images
char = pygame.image.load("yeye2.png").convert()
brick = pygame.image.load("brick.png").convert()
brick2 = pygame.image.load("brick.png").convert()

# some variables
global playerPosX
global playerPosY
playerPosX = 0
playerPosY = 100
jumping = False
falling = False
jumpCount = 10
fallCount = 1

while True:
        events()
        
       
        k = pygame.key.get_pressed()

        # left and right
        if k[K_RIGHT]:
                playerPosX += 7
        elif k[K_LEFT]:
                playerPosX -= 7

        # allow the user to jump again
        if not jumping and not falling:
                if k[K_SPACE]:
                        jumping = True

        # check if we should be falling if we're not jumping
        if not jumping:
                playerPosY, falling = shouldBeFalling(playerPosX, playerPosY)

        # handle drawing any jumping (which means were not falling
        if jumping and not falling:
                jumpCount, playerPosY = jump(jumpCount, playerPosY)
                if jumpCount == 0:
                        # reset the variables we need for jumping
                        jumpCount = 10
                        fallCount = 1
                        jumping = False

        # handle drawing any falling
        if falling:
                fallCount, playerPosY = fall(fallCount, playerPosY)
        if playerPosY < 5:
                playerPosY = playerPosY + 550

       
        redrawGameWindow(playerPosX)

        pygame.display.update()
        CLOCK.tick(FPS)
        
        DS.fill(BLACK)
