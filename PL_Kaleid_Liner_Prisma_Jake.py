import pygame, pytmx, sys
from pygame.locals import *

def __init__():
    pygame.init()
    width = 1280
    height = 720

    mousex, mousey = 0, 0

    #map data
    tmx_data = pytmx.load_pygame("Assets/tileset/untitled.tmx")
    map_data = pyscroll.TiledMapData(tmx_data)
    screen_size = (width, height)
    map_layer = pyscroll.BufferedRenderer(map_data, screen_size)
    group = pyscroll.PyscrollGroup(map_layer=map_layer)

    #color data; not useful
    blue_color = pygame.Color(0, 0, 255)
    black_color = pygame.Color(0, 0, 0)

    #example_image = pygame.image.load('Assets/cat.png')

    fps_clock = pygame.time.Clock()
    font_obj = pygame.font.Font('freesansbold.ttf', 32) #have fang pick a font
    msg = "Begin!"
    sound_obj = pygame.mixer.Sound('Assets/oww.wav') #change

    screen = pygame.display.set_mode((width, height), FULLSCREEN)
    width , height = screen.get_size()
    pygame.display.set_caption('Pilot Light/kaleid liner Prisma Jake')

def MainLoop():
    while True:
        screen.fill(black_color)

        pygame.draw.circle(screen, blue_color, (width/2, height/2), 20, 0)
        pygame.draw.line(screen, blue_color, (width/2, height/2), (mousex, mousey), 4)

        #screen.blit(catSurfaceObj, (mousex, mousey))

        msg_surface_obj = font_obj.render(msg, False, blue_color)
        msg_rect_obj = msg_surface_obj.get_rect()
        msg_rect_obj.topleft = (50, 50)
        screen.blit(msg_surface_obj, msg_rect_obj)

        for event in pygame.event.get():
        	if event.type == QUIT:
        		pygame.quit()
        		sys.exit()
        	elif event.type == MOUSEMOTION:
        		mousex, mousey = event.pos
        	elif event.type == MOUSEBUTTONUP:
        		mousex, mousey = event.pos
        		sound_obj.play()
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
        			pygame.event.post(pygame.event.Event(QUIT))

	pygame.display.update()
	fps_clock.tick(30)

__init__()
MainLoop()
