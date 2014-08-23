import pygame# as pygame
import sys
from pygame.locals import *

class PyManMain:
    def __init__(self, width=640,height=480):
        pygame.init()
        pygamewidth = width
        pygameheight = height
        pygameredColor = pygame.Color(255, 0, 0)
        pygamegreenColor = pygame.Color(0, 255, 0)
        pygameblueColor = pygame.Color(0, 0, 255)
        pygamewhiteColor = pygame.Color(255, 255, 255)
        pygamemousex, pygamemousey = 0, 0

        pygamecatSurfaceObj = pygame.image.load('Assets/cat.png')

        pygamefpsClock = pygame.time.Clock()
        pygamefontObj = pygame.font.Font('freesansbold.ttf', 32)
        pygamemsg = "LD30 BITCH!"
        pygamesoundObj = pygame.mixer.Sound('Assets/oww.wav')

        pygamescreen = pygame.display.set_mode((pygamewidth, pygameheight))
    	pygame.display.set_caption('LD30 BITCH')

    def MainLoop(self):
	    while True:
	        pygamescreen.fill(pygamewhiteColor)


	        pixArr = pygame.PixelArray(pygamescreen)
	        for x in range(100, 200, 4):
	        	for y in range(100, 200, 4):
	        		pixArr[x][y] = pygameredColor
	        del pixArr

	        pygamescreen.blit(pygamecatSurfaceObj, (pygamemousex, pygamemousey))

	        msgSurfaceObj = pygamefontObj.render(pygamemsg, False, pygameblueColor)
	        msgRectobj = msgSurfaceObj.get_rect()
	        msgRectobj.topleft = (10, 20)
	        pygamescreen.blit(msgSurfaceObj, msgRectobj)

	        for event in pygame.event.get():
	        	if event.type == QUIT:
	        		pygame.quit()
	        		sys.exit()
	        	elif event.type == MOUSEMOTION:
	        		pygamemousex, pygamemousey = event.pos
	        	elif event.type == MOUSEBUTTONUP:
	        		pygamemousex, pygamemousey = event.pos
	        		pygamesoundObj.play()
	        		if event.button in (1, 2, 3):
	        			pygamemsg = 'left, middle, or right mouse click'
	        		elif event.button in (4, 5):
	        			pygamemsg = 'mouse scrolled up or down'

	        	elif event.type == KEYDOWN:
	        		if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
	        			pygamemsg = 'Arrow key pressed.'
	        		if event.key == K_a:
	        			pygamemsg = '"A" key pressed'
	        		if event.key == K_ESCAPE:
	        			pygame.event.post(pygame.event.Event(QUIT))

		pygame.display.update()
		pygamefpsClock.tick(30)

if __name__ == "__main__":
 	MainWindow = PyManMain()
	MainWindow.MainLoop()
