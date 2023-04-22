import pygame
import src.constants as const


class VerticalWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(const.wall,
                                            (const.PIECE_SIZE + 8, (const.PIECE_SIZE + 8) * 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HorizontalWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(const.wall,
                                            ((const.PIECE_SIZE + 8) * 4, const.PIECE_SIZE + 8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


LEVEL_1 = [VerticalWall(x, y) for y in range(35, 500, 170) for x in range(80, 700, 170)]

LEVEL_2 = [HorizontalWall(x, y) for y in range(60, 500, 120) for x in range(55, 700, 170)]

LEVEL_3 = [HorizontalWall(x, y) for y in range(70, 500, 170) for x in range(55, 700, 170)]
[LEVEL_3.append(VerticalWall(x, y)) for y in range(40, 500, 170) for x in range(90, 700, 170)]

LEVEL_4 = [HorizontalWall(50 + x, x) for x in range(30, 480, 60)]
[LEVEL_4.append(HorizontalWall(50 + y, 510 - y)) for y in range(480, 30, -60)]

LEVEL_5 = [HorizontalWall(x, y) for y in range(30, 500, 85) for x in range(55, 700, 170)]
[LEVEL_5.append(VerticalWall(x, y)) for y in range(30, 500, 170) for x in range(90, 700, 170)]


def wall_generation(mode):
    walls = pygame.sprite.Group()
    if mode == 1:
        for i in LEVEL_1:
            walls.add(i)
    elif mode == 2:
        for i in LEVEL_2:
            walls.add(i)
    elif mode == 3:
        for i in LEVEL_3:
            walls.add(i)
    elif mode == 4:
        for i in LEVEL_4:
            walls.add(i)
    elif mode == 5:
        for i in LEVEL_5:
            walls.add(i)
    return walls
