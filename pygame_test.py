import pygame# as pygame
import sys
from pygame.locals import *

class PyManMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.redColor = pygame.Color(255, 0, 0)
        self.greenColor = pygame.Color(0, 255, 0)
        self.blueColor = pygame.Color(0, 0, 255)
        self.whiteColor = pygame.Color(255, 255, 255)
        self.mousex, self.mousey = 0, 0

        self.catSurfaceObj = pygame.image.load('Assets/cat.png')

        self.fpsClock = pygame.time.Clock()
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.msg = "LD30 BITCH!"
        self.soundObj = pygame.mixer.Sound('Assets/oww.wav')

        self.screen = pygame.display.set_mode((self.width, self.height))
    	pygame.display.set_caption('LD30 BITCH')

    def MainLoop(self):
	    while True:
	        self.screen.fill(self.whiteColor)

	        pygame.draw.circle(self.screen, self.blueColor, (self.width/2, self.height/2), 20, 0)
	        pygame.draw.line(self.screen, self.blueColor, (self.width/2, self.height/2), (self.mousex, self.mousey), 4)

	        pixArr = pygame.PixelArray(self.screen)
	        for x in range(100, 200, 4):
	        	for y in range(100, 200, 4):
	        		pixArr[x][y] = self.redColor
	        del pixArr

	        self.screen.blit(self.catSurfaceObj, (self.mousex, self.mousey))

	        msgSurfaceObj = self.fontObj.render(self.msg, False, self.blueColor)
	        msgRectobj = msgSurfaceObj.get_rect()
	        msgRectobj.topleft = (10, 20)
	        self.screen.blit(msgSurfaceObj, msgRectobj)

	        for event in pygame.event.get():
	        	if event.type == QUIT:
	        		pygame.quit()
	        		sys.exit()
	        	elif event.type == MOUSEMOTION:
	        		self.mousex, self.mousey = event.pos
	        	elif event.type == MOUSEBUTTONUP:
	        		self.mousex, self.mousey = event.pos
	        		self.soundObj.play()
	        		if event.button in (1, 2, 3):
	        			self.msg = 'left, middle, or right mouse click'
	        		elif event.button in (4, 5):
	        			self.msg = 'mouse scrolled up or down'

	        	elif event.type == KEYDOWN:
	        		if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
	        			self.msg = 'Arrow key pressed.'
	        		if event.key == K_a:
	        			self.msg = '"A" key pressed'
	        		if event.key == K_ESCAPE:
	        			pygame.event.post(pygame.event.Event(QUIT))

		pygame.display.update()
		self.fpsClock.tick(30)

if __name__ == "__main__":
 	MainWindow = PyManMain()
	MainWindow.MainLoop()
