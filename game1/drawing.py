import math

from map import world_map
from map import mini_map
from settings import *
import pygame
from ray_casting import ray_casting
class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'1':pygame.image.load('textures/wall1.png').convert(),
                        '2':pygame.image.load('textures/wall2.png').convert(),
                        's':pygame.image.load('textures/sky.png').convert()}
    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['s'], (sky_offset, 0))
        self.sc.blit(self.textures['s'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['s'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGREY, (0, 400, WIDTH, HEIGHT_HALF))
    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, DARKGORANGE)
        self.sc.blit(render, (WIDTH - 65, 5))
    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
        pygame.draw.line(self.sc_map, YELLOW, (map_x,map_y), (map_x + 12 * math.cos(player.angle),
                                                               map_y + 12 * math. sin(player.angle)), 2)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, DARKGROWN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

