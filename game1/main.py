import pygame
import math
pygame.init()
from settings import *
from player import player
from map import *
from ray_casting import ray_casting
from drawing import Drawing
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
pygame.display.set_caption("game1")
clock = pygame.time.Clock()
player = player()
drawing = Drawing(sc, sc_map)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)
    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.update()
    clock.tick(FPS)

