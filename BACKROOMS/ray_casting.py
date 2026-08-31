import math
import pygame
from settings import *
from map import world_map
def ray_casting(sc, plyer_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = plyer_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a

            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_hight = PROJ_COEF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c // 2, c, c // 3)
                pygame.draw.rect(sc, color, (ray * SCALE, HEIGHT_HALF - proj_hight // 2, SCALE, proj_hight))
                break
        cur_angle += DELTA_ANGLE