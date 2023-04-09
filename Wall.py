import pygame
import random
import constants as const


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(const.brick.convert_alpha(), (const.PIECE_SIZE + 8, const.PIECE_SIZE + 8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.rect.x = random.randrange(0, const.WIDTH - self.rect.width - 10, const.PIECE_SIZE - 10)
        # self.rect.y = random.randrange(0, const.HEIGHT - self.rect.height - 10, const.PIECE_SIZE - 10)

