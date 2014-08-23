import pygame as pg
import sys
from pygame.locals import *

pg.init()
fpsClock = pg.time.Clock()

windowSurfaceObj = pg.display.set_mode((640, 480))
pg,display.set_caption('pg Test Page')

redColor      = pg.Color(255, 0, 0)
greenColor    = pg.Color(0, 255, 0)
blueColor     = pg.Color(0, 0, 255)
whiteColor    = pg.Color(255, 255, 255)
mousex, mousey = 0, 0

fonyObj = pg.font.Font('freesansbold.ttf', 32)
msg = "LD30 BITCH!"

soundObj = pg.mixer.Sound('oww.wav')


while True:
	windowSurfaceObj.fill(whiteColor)

	pg.draw.polygon(windowSurfaceObj, greenColor, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
	pg.draw.circle(windowSurfaceObj, blueColor, (300, 50), 20, 0)
	pg.draw.ellipse(windowSurfaceObj, redColor, (300, 250, 40, 80), 1)
	pg.draw.rect(windowSurfaceObj, redColor, (10, 10, 50, 100))
	pg.draw.line(windowSurfaceObj, blueColor, (60, 160), (120, 60), 4)

	pixArr = pg.PixelArray(windowSurfaceObj)
	for x in range(100, 200, 4):
		for y in range(100, 200, 4):
			pixArr[x][y] = redColor
		del pixArr

	windowSurfaceObj.blit(catSurfaceObj, (mousex, mousey))

	msgSurfaceObj = fontObj.render(msg, False, blueColor)
	msgRectobj = msgSurfaceObj.get_rect()
	msgRectobj.topleft = (10, 20)
	windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		elif event.tyoe == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			soundObj.play()
			if event.button in (1, 2, 3):
				msg = 'left, middle, or right mouse click'
			elif event.button in (4, 5):
				msg = 'mouse scrolled up or down'

		elif event.type == KEYDOWN:
			if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
				msg = 'Arrow key pressed.'
			if event.key == K_a:
				msg = '"A" key pressed'
			if event.key == K_ESCAPE:
				pg.event.post(pg.event.Event(QUIT))

	pg.display.update()
	fpsClock.tick(30)





