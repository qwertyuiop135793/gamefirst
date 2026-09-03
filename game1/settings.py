#game settings
import math
#screen set
import pygame
WIDTH = 1200
HEIGHT = 800
WIDTH_HALF = WIDTH // 2
HEIGHT_HALF = HEIGHT // 2
TILE = 100
FPS = 580

#minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

#ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 880
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

#sprite settings


#texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE


#player settings
player_pos = (WIDTH_HALF // 4, HEIGHT_HALF - 50)
player_angle = 0
player_speed = 2

#colors
BLACK = (0, 0, 0)
GREEN = (0, 80, 0)
DARKGREY = (40, 40, 40)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SKYBLUE = (0, 186, 255)
RED = (255, 0, 0)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARKGROWN = (97, 61, 25)
DARKGORANGE = (255, 140, 0)