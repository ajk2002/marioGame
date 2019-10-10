

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
longbrick = pygame.image.load("bricking.png").convert()
num = random.randint(0,20)
class player(object):
	def_init_(self, marioWidth, marioLen, marioPosX, playerPosX, playerPosY, playerVelocityX, marioPos, mariomove, vel, isJump, jumpCount):
		self.marioWidth = marioWidth
		self.marioLen = marioLen
		self.marioPosX = marioPosX
		self.playerPosX = playerPosX
		self.playerPosY = playerPosY
		self.playerVelocityX = playerVelocityX
		self.marioPos = marioPos
		self.mariomove = mariomove
		self.vel = vel
		self.isJump = isJump
		self.jumpCount = jumpCount
bgWidth, bgHeight = bg.get_rect().size


stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW


vel = 100
brickX = random.randint(1,400)
brickY = random.randint(10, 700)
brickX1 = random.randint(1,400)
brickY1 = random.randint(10, 700)

brickMove = 0
brickArray = []
isJump = False
jumpCount = 10

man = player(300,410,64,64)
# def grid():
# 	global picked
# 	for i in range(1, 40):
# 		brickArray.append((i * 32) - 1)
#
# 	picked = random.choice(brickArray)
#
# 	#draw a brick at position x picked
#
# def brick():
# 	bricks = []
# 	 #we are going to create an array of n bricks, each with x and y coords
# 	for i in range(5):
# 		bricks.append = ((i * 10) + 1 )
#
# 	print(bricks)



# grid()
# brick()


# main loop
while True:

	events()



	k = pygame.key.get_pressed()

	if k[K_RIGHT]:
		man.playerVelocityX = 7
		man.playerPosX += man.playerVelocityX


	elif k[K_LEFT]:
		man.playerVelocityX = -7
		man.playerPosX += man.playerVelocityX

	if not k[K_RIGHT]:
		man.playerVelocityX = 0

	if not (isJump):
		if k[pygame.K_SPACE]:
			man.isJump = True
		
	else:

		
		#stagePosX += -playerVelocityX #not 
		if man.jumpCount >= -10:
			
			neg = 1
			if man.jumpCount < 0:
				neg = -1
			man.playerPosY -= (man.jumpCount ** 2) * 0.5 * neg
			man.jumpCount -= 1
		else:
			man.isJump = False
			man.jumpCount = 10



	
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

