import pygame
import src.Wall as Wall

LEVEL_1 = [Wall.VerticalWall(x, y) for y in range(35, 500, 170) for x in range(80, 700, 170)]

LEVEL_2 = [Wall.HorizontalWall(x, y) for y in range(60, 500, 120) for x in range(55, 700, 170)]

LEVEL_3 = [Wall.HorizontalWall(x, y) for y in range(70, 500, 170) for x in range(55, 700, 170)]
[LEVEL_3.append(Wall.VerticalWall(x, y)) for y in range(40, 500, 170) for x in range(90, 700, 170)]

LEVEL_4 = [Wall.HorizontalWall(50 + x, x) for x in range(30, 480, 60)]
[LEVEL_4.append(Wall.HorizontalWall(50 + y, 510 - y)) for y in range(480, 30, -60)]

LEVEL_5 = [Wall.HorizontalWall(x, y) for y in range(30, 500, 85) for x in range(55, 700, 170)]
[LEVEL_5.append(Wall.VerticalWall(x, y)) for y in range(30, 500, 170) for x in range(90, 700, 170)]

LEVELS = [LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5]


def generation(level_id):
    walls = pygame.sprite.Group()
    if level_id == 0:
        pass
    else:
        for i in LEVELS[level_id - 1]:
            walls.add(i)
    return walls
