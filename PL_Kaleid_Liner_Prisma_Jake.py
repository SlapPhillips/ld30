import os.path
import pytmx
import pygame
import pyscroll
import pyscroll.data
import sys
from pyscroll.util import PyscrollGroup
from pygame.locals import *

# define configuration variables here
MAP_DIR = 'Assets/tileset'

HERO_MOVE_SPEED = 240            # pixels per second
MAP_FILENAME = 'grasslands.tmx'

# used for 2x scaling
temp_surface = None

# simple wrapper to keep the screen resizeable
def init_screen(width, height):
    global temp_surface
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    temp_surface = pygame.Surface((width / 2, height / 2)).convert()
    return screen

# make loading maps a little easier
def get_map(filename):
    return os.path.join(MAP_DIR, filename)


# make loading images a little easier
def load_image(filename):
    return pygame.image.load(os.path.join(MAP_DIR, filename))

class Hero(pygame.sprite.Sprite):
    """ Our Hero

    The Hero has three collision rects, one for the whole sprite "rect" and
    "old_rect", and another to check collisions with walls, called "feet".

    The position list is used because pygame rects are inaccurate for
    positioning sprites; because the values they get are 'rounded down' to
    as integers, the sprite would move faster moving left or up.

    Feet is 1/2 as wide as the normal rect, and 8 pixels tall.  This size
    allows the top of the sprite to overlap walls.

    There is also an old_rect that is used to reposition the sprite if it
    collides with level walls.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('hero.png').convert_alpha()
        self.velocity = [0, 0]
        self._position = [0, 0]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * .5, 8)

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        """ If called after an update, the sprite can move back
        """
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

class QuestGame(object):
    """ This class is a basic game.

    This class will load data, create a pyscroll group, a hero object.
    It also reads input and moves the Hero around the map.
    Finally, it uses a pyscroll group to render the map and Hero.
    """
    filename = get_map(MAP_FILENAME)

    def __init__(self):

        # true while running
        self.running = False

        # load data from pytmx
        tmx_data = pytmx.load_pygame(self.filename)

        # setup level geometry with simple pygame rects, loaded from pytmx
        self.walls = list()
        for object in tmx_data.objects:
            self.walls.append(pygame.Rect(
                object.x, object.y,
                object.width, object.height))

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)

        w, h = screen.get_size()

        # create new renderer (camera)
        # clamp_camera is used to prevent the map from scrolling past the edge
        self.map_layer = pyscroll.BufferedRenderer(map_data,
                                                   (w / 2, h / 2),
                                                   clamp_camera=True)

        # pyscroll supports layered rendering.  our map has 3 'under' layers
        # layers begin with 0, so the layers are 0, 1, and 2.
        # since we want the sprite to be on top of layer 1, we set the default
        # layer for sprites as 1
        self.group = PyscrollGroup(map_layer=self.map_layer,
                                   default_layer=2)

        self.hero = Hero()

        # put the hero in the center of the map
        self.hero.position = self.map_layer.rect.center

        # add our hero to the group
        self.group.add(self.hero)

    def draw(self, surface):

        # center the map/screen on our Hero
        self.group.center(self.hero.rect.center)

        # draw the map and all sprites
        self.group.draw(surface)

    def handle_input(self):
        """ Handle pygame input events
        """
        event = pygame.event.poll()
        while event:
            if event.type == QUIT:
                self.running = False
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    break

            # this will be handled if the window is resized
            elif event.type == VIDEORESIZE:
                init_screen(event.w, event.h)
                self.map_layer.set_size((event.w / 2, event.h / 2))

            event = pygame.event.poll()

        # using get_pressed is slightly less accurate than testing for events
        # but is much easier to use.
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            self.hero.velocity[1] = -HERO_MOVE_SPEED
        elif pressed[K_DOWN]:
            self.hero.velocity[1] = HERO_MOVE_SPEED
        else:
            self.hero.velocity[1] = 0

        if pressed[K_LEFT]:
            self.hero.velocity[0] = -HERO_MOVE_SPEED
        elif pressed[K_RIGHT]:
            self.hero.velocity[0] = HERO_MOVE_SPEED
        else:
            self.hero.velocity[0] = 0

    def update(self, dt):
        """ Tasks that occur over time should be handled here
        """
        self.group.update(dt)

        # check if the sprite's feet are colliding with wall
        # sprite must have a rect called feet, and move_back method,
        # otherwise this will fail
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back(dt)

    def run(self):
        """ Run the game loop
        """
        clock = pygame.time.Clock()
        fps = 60
        scale = pygame.transform.scale
        self.running = True

        try:
            while self.running:
                dt = clock.tick(fps) / 1000.

                self.handle_input()
                self.update(dt)
                self.draw(temp_surface)
                scale(temp_surface, screen.get_size(), screen)
                pygame.display.flip()

        except KeyboardInterrupt:
            self.running = False


if __name__ == "__main__":
    pygame.init()
<<<<<<< HEAD
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
=======
    pygame.font.init()
    screen = init_screen(800, 600)
    pygame.display.set_caption('Quest - An epic journey.')

    try:
        game = QuestGame()
        game.run()
    except:
        pygame.quit()
        raise
>>>>>>> FETCH_HEAD
