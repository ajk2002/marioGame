

import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():        
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()


# define display surface			
W, H = 1280, 800
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 30

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bg = pygame.image.load("mountains.png").convert()

char = pygame.image.load("yeye2.png").convert()
brick = pygame.image.load("brick.png").convert()
longbrick = pygame.image.load("longbrick.png")



bgWidth, bgHeight = bg.get_rect().size
marioWidth = 650
stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

marioLen = 100
marioPosX = marioLen


playerPosX = 50
playerPosY = 700
playerVelocityX = 0
marioPos = 400
mariomove = 0
vel = 100
brickX = random.randint(1,400)
brickY = random.randint(10, 700)
brickX1 = random.randint(1,400)
brickY1 = random.randint(10, 700)

brickMove = 0
blockSize = 10
isJump = False
jumpCount = 10
brickArray = []

boxX = 200
boxY = 400
hitbox = (boxX , boxY , 160, 56)








# main loop
while True:

	events()
	for i in range(1, 40):
		brickArray.append((i * 32) - 1)
###


	k = pygame.key.get_pressed()

	if k[K_RIGHT]:
		playerVelocityX = 7
		playerPosX += playerVelocityX


	elif k[K_LEFT]:
		playerVelocityX = -7
		playerPosX += playerVelocityX

	if not k[K_RIGHT]:
		playerVelocityX = 0

	if not (isJump):
		if k[pygame.K_SPACE]:
			isJump = True
		
	else:

		
		#stagePosX += -playerVelocityX #not 
		if jumpCount >= -10:
			
			neg = 1
			if jumpCount < 0:
				neg = -1
			playerPosY -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10



	
		#print("only at start")
		#playerVelocityX = 0
	#     stops player from going off the stage on the left and right 		
	
	#playerVelocityX = 0	
	if playerPosX > stageWidth - marioWidth: playerPosX = stageWidth - marioWidth
	if playerPosX > marioWidth: playerPosX = marioWidth
	if playerPosX < startScrollingPosX:marioPosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX:circlePosX = playerPosX - stageWidth + W
	else:
		marioPosX = startScrollingPosX
		stagePosX += -playerVelocityX
		brickMove -= playerVelocityX
	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth,0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))
		
	DS.blit(char, (marioPosX, playerPosY))

	DS.blit(brick, (brickX1 + brickMove, brickY1))
	pygame.draw.rect(DS, (255, 0, 0), hitbox, 2)
	DS.blit(longbrick, (200 , 400))
	if playerPosX > stageWidth - marioLen:playerPosX = stageWidth - marioLen
	if playerPosX < marioLen: playerPosX = marioLen
	if playerPosX < startScrollingPosX: circlePosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX:
		# centre of screen now
		
		circlePosX = playerPosX - stageWidth + W
	else:
		circlePosX = startScrollingPosX
		stagePosX += -playerVelocityX
	
	rel_x = stagePosX % bgWidth

       
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)

