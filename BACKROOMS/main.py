import pygame
import math
pygame.init()
from settings import *
from player import player
from map import *
from ray_casting import ray_casting
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)
    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HEIGHT_HALF))
    pygame.draw.rect(sc, DARKGREY, (0, 800, WIDTH, HEIGHT_HALF))
    ray_casting(sc, player.pos, player.angle)


    pygame.display.update()
    clock.tick(FPS)

