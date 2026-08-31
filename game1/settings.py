#game settings
import math
#screen set
import pygame
WIDTH = 1200
HEIGHT = 800
WIDTH_HALF = WIDTH // 2
HEIGHT_HALF = HEIGHT // 2
TILE = 100
FPS = 60

#ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 80
MAX_DEPTH = 880
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

#player settings
player_pos = (WIDTH_HALF, HEIGHT_HALF)
player_angle = 0
player_speed = 2

#colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARKGREY = (54, 55, 55)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)

