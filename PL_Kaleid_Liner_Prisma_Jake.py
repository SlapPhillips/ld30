import pygame, pytmx, sys
from pygame.locals import *

class PrismaJakeMain:
    def __init__(self):
        pygame.init()
        self.width = 1280
        self.height = 720

        self.mousex, self.mousey = 0, 0

        #map data
        tmx_data = pytmx.load_pygame("untitled.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        screen_size = (self.width, self.height)
        map_layer = pyscroll.BufferedRenderer(map_data, screen_size)
        group = pyscroll.PyscrollGroup(map_layer=map_layer)

        #color data; not useful
        self.red_color = pygame.Color(255, 0, 0)
        self.green_color = pygame.Color(0, 255, 0)
        self.blue_color = pygame.Color(0, 0, 255)
        self.white_color = pygame.Color(255, 255, 255)
        self.black_color = pygame.Color(0, 0, 0)

        #self.example_image = pygame.image.load('Assets/cat.png')

        self.fps_clock = pygame.time.Clock()
        self.font_obj = pygame.font.Font('freesansbold.ttf', 32) #have fang pick a font
        self.msg = "Begin!"
        self.sound_obj = pygame.mixer.Sound('Assets/oww.wav') #change

        self.screen = pygame.display.set_mode((self.width, self.height), FULLSCREEN)
    	self.width , self.height = self.screen.get_size()
    	pygame.display.set_caption('Pilot Light/kaleid liner Prisma Jake')

    def MainLoop(self):
	    while True:
	        self.screen.fill(self.black_color)

	        pygame.draw.circle(self.screen, self.blue_color, (self.width/2, self.height/2), 20, 0)
	        pygame.draw.line(self.screen, self.blue_color, (self.width/2, self.height/2), (self.mousex, self.mousey), 4)

	        #self.screen.blit(self.catSurfaceObj, (self.mousex, self.mousey))

	        msg_surface_obj = self.font_obj.render(self.msg, False, self.blue_color)
	        msg_rect_obj = msg_surface_obj.get_rect()
	        msg_rect_obj.topleft = (10, 20)
	        self.screen.blit(msg_surface_obj, msg_rect_obj)

	        for event in pygame.event.get():
	        	if event.type == QUIT:
	        		pygame.quit()
	        		sys.exit()
	        	elif event.type == MOUSEMOTION:
	        		self.mousex, self.mousey = event.pos
	        	elif event.type == MOUSEBUTTONUP:
	        		self.mousex, self.mousey = event.pos
	        		self.sound_obj.play()
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
		self.fps_clock.tick(30)

if __name__ == "__main__":
 	MainWindow = PrismaJakeMain()
	MainWindow.MainLoop()
