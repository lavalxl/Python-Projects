import pygame
import src.constants as const


class VerticalWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(const.wall,
                                            (const.WALL_SIZE, const.WALL_SIZE * 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HorizontalWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(const.wall,
                                            (const.WALL_SIZE * 4, const.WALL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

